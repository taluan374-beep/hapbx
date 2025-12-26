"""
Image Generation Service
Supports: DALL-E 3, Flux (via Replicate)
"""
import os
import time
from typing import Dict, Any, Optional, List
from openai import OpenAI
import replicate
import httpx

from ...config import settings


class ImageGenerator:
    """Image generation service with multiple providers"""
    
    def __init__(self):
        self.openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    def generate_dalle(
        self,
        prompt: str,
        size: str = "1024x1024",
        quality: str = "hd",
        style: str = "natural"  # natural or vivid
    ) -> Dict[str, Any]:
        """
        Generate image with DALL-E 3
        Best for: Product mockups, clean designs, specific compositions
        
        Args:
            prompt: Image description
            size: 1024x1024, 1792x1024, or 1024x1792
            quality: standard or hd
            style: natural or vivid
        """
        start_time = time.time()
        
        response = self.openai_client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=quality,
            style=style,
            n=1
        )
        
        return {
            "success": True,
            "provider": "dalle-3",
            "image_url": response.data[0].url,
            "revised_prompt": response.data[0].revised_prompt,
            "generation_time_seconds": round(time.time() - start_time, 2)
        }
    
    def generate_flux(
        self,
        prompt: str,
        aspect_ratio: str = "1:1",
        output_format: str = "webp",
        output_quality: int = 90
    ) -> Dict[str, Any]:
        """
        Generate image with Flux (via Replicate)
        Best for: Photorealistic, artistic styles, portraits
        
        Args:
            prompt: Image description
            aspect_ratio: 1:1, 16:9, 9:16, 4:3, 3:4, etc.
            output_format: webp, png, jpg
            output_quality: 1-100
        """
        start_time = time.time()
        
        output = replicate.run(
            "black-forest-labs/flux-1.1-pro",
            input={
                "prompt": prompt,
                "aspect_ratio": aspect_ratio,
                "output_format": output_format,
                "output_quality": output_quality
            }
        )
        
        # Flux returns a FileOutput object or URL
        image_url = str(output) if output else None
        
        return {
            "success": True,
            "provider": "flux-1.1-pro",
            "image_url": image_url,
            "generation_time_seconds": round(time.time() - start_time, 2)
        }
    
    def generate_flux_schnell(
        self,
        prompt: str,
        aspect_ratio: str = "1:1",
        num_outputs: int = 1
    ) -> Dict[str, Any]:
        """
        Generate image with Flux Schnell (faster, cheaper)
        Best for: Quick iterations, drafts
        """
        start_time = time.time()
        
        output = replicate.run(
            "black-forest-labs/flux-schnell",
            input={
                "prompt": prompt,
                "aspect_ratio": aspect_ratio,
                "num_outputs": num_outputs,
                "output_format": "webp",
                "output_quality": 80
            }
        )
        
        # Returns list of URLs
        image_urls = [str(url) for url in output] if output else []
        
        return {
            "success": True,
            "provider": "flux-schnell",
            "image_urls": image_urls,
            "generation_time_seconds": round(time.time() - start_time, 2)
        }
    
    async def generate(
        self,
        prompt: str,
        provider: str = "dalle",
        **kwargs
    ) -> Dict[str, Any]:
        """
        Main generation method - routes to appropriate provider
        
        Args:
            prompt: Image description
            provider: dalle, flux, flux_schnell
            **kwargs: Provider-specific arguments
        """
        providers = {
            "dalle": self.generate_dalle,
            "flux": self.generate_flux,
            "flux_schnell": self.generate_flux_schnell,
        }
        
        generator = providers.get(provider)
        if not generator:
            raise ValueError(f"Unknown provider: {provider}. Available: {list(providers.keys())}")
        
        return generator(prompt, **kwargs)


class MarketingImagePrompts:
    """Helper class to build marketing-specific image prompts"""
    
    @staticmethod
    def product_showcase(
        product_name: str,
        product_description: str,
        style: str = "modern",
        background: str = "clean white studio",
        mood: str = "professional"
    ) -> str:
        """Generate prompt for product photography style images"""
        return f"""Professional product photography of {product_name}.
Product description: {product_description}

Style: {style}, high-end commercial photography
Background: {background}
Mood: {mood}
Lighting: Soft studio lighting with gentle shadows
Composition: Centered product, rule of thirds, negative space for text
Quality: 8K, ultra detailed, photorealistic

NO text, NO watermarks, NO logos in the image."""

    @staticmethod
    def social_media_post(
        theme: str,
        brand_colors: List[str],
        mood: str = "modern",
        platform: str = "instagram"
    ) -> str:
        """Generate prompt for social media post graphics"""
        colors_str = ", ".join(brand_colors) if brand_colors else "vibrant colors"
        
        aspect_ratios = {
            "instagram": "square 1:1",
            "instagram_story": "vertical 9:16",
            "facebook": "landscape 16:9",
            "linkedin": "landscape 1.91:1"
        }
        
        return f"""Social media post design for {platform}.
Theme: {theme}
Color palette: {colors_str}
Mood: {mood}, clean, professional

Style: Modern graphic design, minimalist
Composition: {aspect_ratios.get(platform, 'square')} format
Leave 30% negative space for text overlay
Abstract shapes and gradients
Suitable for marketing content

NO text, NO watermarks, clean design only."""

    @staticmethod
    def ads_banner(
        product: str,
        style: str = "modern",
        emotion: str = "excitement"
    ) -> str:
        """Generate prompt for advertising banners"""
        return f"""Digital advertising banner design.
Product: {product}
Style: {style}, high-converting ad design
Emotion to evoke: {emotion}

Layout: Product prominently displayed
Leave space on right side for headline and CTA
Colors: Vibrant, high contrast, attention-grabbing
Lighting: Dramatic, professional

Quality: High resolution, suitable for digital ads
NO text in the image, design only."""

    @staticmethod
    def lifestyle_shot(
        product: str,
        setting: str,
        target_audience: str,
        mood: str = "aspirational"
    ) -> str:
        """Generate prompt for lifestyle photography"""
        return f"""Lifestyle photography featuring {product}.
Setting: {setting}
Target audience: {target_audience}
Mood: {mood}, authentic, relatable

Style: Editorial lifestyle photography
Natural lighting, candid feel
Show product in use naturally
Warm, inviting atmosphere

Quality: 8K, professional photography
NO text, NO obvious branding."""

    @staticmethod
    def before_after(
        topic: str,
        before_state: str,
        after_state: str
    ) -> str:
        """Generate prompt for before/after comparison images"""
        return f"""Split comparison image showing transformation.
Topic: {topic}

Left side (Before): {before_state}
Right side (After): {after_state}

Style: Clean, professional, clear difference visible
Lighting: Consistent on both sides
Same angle, same composition, different states

NO text, NO labels, visual comparison only."""


# Example usage and generation helpers
class ContentImageGenerator:
    """High-level image generation for content marketing"""
    
    def __init__(self):
        self.generator = ImageGenerator()
        self.prompts = MarketingImagePrompts()
    
    async def generate_for_social_post(
        self,
        brand_name: str,
        brand_colors: List[str],
        post_theme: str,
        platform: str = "instagram",
        provider: str = "dalle"
    ) -> Dict[str, Any]:
        """Generate image suitable for social media post"""
        
        prompt = self.prompts.social_media_post(
            theme=f"{brand_name} - {post_theme}",
            brand_colors=brand_colors,
            platform=platform
        )
        
        size_map = {
            "instagram": "1024x1024",
            "instagram_story": "1024x1792",
            "facebook": "1792x1024",
        }
        
        if provider == "dalle":
            return await self.generator.generate(
                prompt=prompt,
                provider="dalle",
                size=size_map.get(platform, "1024x1024")
            )
        else:
            aspect_map = {
                "instagram": "1:1",
                "instagram_story": "9:16",
                "facebook": "16:9",
            }
            return await self.generator.generate(
                prompt=prompt,
                provider=provider,
                aspect_ratio=aspect_map.get(platform, "1:1")
            )
    
    async def generate_product_image(
        self,
        product_name: str,
        product_description: str,
        style: str = "modern",
        provider: str = "flux"
    ) -> Dict[str, Any]:
        """Generate product showcase image"""
        
        prompt = self.prompts.product_showcase(
            product_name=product_name,
            product_description=product_description,
            style=style
        )
        
        return await self.generator.generate(
            prompt=prompt,
            provider=provider
        )
    
    async def generate_ad_creative(
        self,
        product: str,
        ad_style: str = "modern",
        emotion: str = "excitement",
        provider: str = "dalle"
    ) -> Dict[str, Any]:
        """Generate advertising creative"""
        
        prompt = self.prompts.ads_banner(
            product=product,
            style=ad_style,
            emotion=emotion
        )
        
        return await self.generator.generate(
            prompt=prompt,
            provider=provider,
            size="1792x1024" if provider == "dalle" else None,
            aspect_ratio="16:9" if provider != "dalle" else None
        )
