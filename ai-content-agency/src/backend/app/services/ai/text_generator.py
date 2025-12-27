"""
Text Generation Service
Multi-provider support: OpenAI, Anthropic
"""
import json
import time
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from openai import OpenAI
from anthropic import Anthropic

from ...config import settings
from .prompts import PromptBuilder, INDUSTRY_EXAMPLES


class LLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str, temperature: float = 0.7) -> tuple[str, Dict]:
        """Generate text and return (content, usage_info)"""
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI GPT-4o provider"""
    
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = "gpt-4o"
    
    def generate(self, system_prompt: str, user_prompt: str, temperature: float = 0.7) -> tuple[str, Dict]:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
            max_tokens=4000,
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        usage = {
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }
        
        return content, usage


class AnthropicProvider(LLMProvider):
    """Anthropic Claude provider"""
    
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.model = "claude-3-5-sonnet-20241022"
    
    def generate(self, system_prompt: str, user_prompt: str, temperature: float = 0.7) -> tuple[str, Dict]:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=4000,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt + "\n\nRespond with valid JSON only."}
            ],
            temperature=temperature
        )
        
        content = response.content[0].text
        usage = {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "total_tokens": response.usage.input_tokens + response.usage.output_tokens
        }
        
        return content, usage


class TextGenerator:
    """Main text generation service"""
    
    def __init__(self, provider: str = "openai"):
        providers = {
            "openai": OpenAIProvider,
            "anthropic": AnthropicProvider,
        }
        
        if provider not in providers:
            raise ValueError(f"Unknown provider: {provider}. Available: {list(providers.keys())}")
        
        self.provider = providers[provider]()
        self.provider_name = provider
        self.prompt_builder = PromptBuilder()
    
    def _parse_json_response(self, content: str) -> Dict:
        """Parse JSON from LLM response, handling markdown code blocks"""
        # Remove markdown code blocks if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
        
        return json.loads(content.strip())
    
    def _get_industry_example(self, industry: str, content_type: str) -> str:
        """Get industry-specific examples for few-shot learning"""
        industry_data = INDUSTRY_EXAMPLES.get(industry, {})
        return industry_data.get(content_type, "")
    
    def generate_social_content(
        self,
        brand_context: str,
        platform: str,
        objective: str = "engagement",
        topic: str = "",
        product_name: Optional[str] = None,
        key_message: Optional[str] = None,
        promotion: Optional[str] = None,
        body_length: str = "medium",
        num_variations: int = 3,
        industry: Optional[str] = None,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """Generate social media content"""
        
        start_time = time.time()
        
        # Build prompts
        system_prompt = self.prompt_builder.get_system_prompt(brand_context)
        user_prompt = self.prompt_builder.get_social_prompt(
            platform=platform,
            objective=objective,
            topic=topic,
            product_name=product_name,
            key_message=key_message,
            promotion=promotion,
            body_length=body_length,
            num_variations=num_variations
        )
        
        # Add industry examples if available
        if industry:
            example = self._get_industry_example(industry, f"social_{platform}")
            if example:
                user_prompt += f"\n\n## VÍ DỤ THAM KHẢO\n{example}"
        
        # Generate
        content, usage = self.provider.generate(system_prompt, user_prompt, temperature)
        
        # Parse response
        result = self._parse_json_response(content)
        
        return {
            "success": True,
            "content_type": f"social_{platform}",
            "variations": result.get("variations", []),
            "ai_model_used": f"{self.provider_name}/{self.provider.model}",
            "tokens_used": usage,
            "generation_time_seconds": round(time.time() - start_time, 2)
        }
    
    def generate_ads_copy(
        self,
        brand_context: str,
        platform: str,
        product_name: str,
        offer: Optional[str] = None,
        landing_url: Optional[str] = None,
        objective: str = "conversion",
        num_variations: int = 3,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """Generate ads copy"""
        
        start_time = time.time()
        
        system_prompt = self.prompt_builder.get_system_prompt(brand_context)
        user_prompt = self.prompt_builder.get_ads_prompt(
            platform=platform,
            product_name=product_name,
            offer=offer,
            landing_url=landing_url,
            objective=objective,
            num_variations=num_variations
        )
        
        content, usage = self.provider.generate(system_prompt, user_prompt, temperature)
        result = self._parse_json_response(content)
        
        return {
            "success": True,
            "content_type": f"ads_{platform}",
            "variations": result.get("variations", []),
            "a_b_test_recommendation": result.get("a_b_test_recommendation", ""),
            "ai_model_used": f"{self.provider_name}/{self.provider.model}",
            "tokens_used": usage,
            "generation_time_seconds": round(time.time() - start_time, 2)
        }
    
    def generate_landing_page(
        self,
        brand_context: str,
        product_name: str,
        price: Optional[str] = None,
        offer: Optional[str] = None,
        page_type: str = "sales",
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """Generate landing page copy"""
        
        start_time = time.time()
        
        system_prompt = self.prompt_builder.get_system_prompt(brand_context)
        user_prompt = self.prompt_builder.get_landing_page_prompt(
            product_name=product_name,
            price=price,
            offer=offer,
            page_type=page_type
        )
        
        content, usage = self.provider.generate(system_prompt, user_prompt, temperature)
        result = self._parse_json_response(content)
        
        return {
            "success": True,
            "content_type": "landing_page",
            "landing_page": result,
            "ai_model_used": f"{self.provider_name}/{self.provider.model}",
            "tokens_used": usage,
            "generation_time_seconds": round(time.time() - start_time, 2)
        }
    
    def generate_video_script(
        self,
        brand_context: str,
        platform: str,
        duration: int,
        topic: str,
        product_name: Optional[str] = None,
        video_style: str = "talking_head",
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """Generate video script"""
        
        start_time = time.time()
        
        system_prompt = self.prompt_builder.get_system_prompt(brand_context)
        user_prompt = self.prompt_builder.get_video_script_prompt(
            platform=platform,
            duration=duration,
            topic=topic,
            product_name=product_name,
            video_style=video_style
        )
        
        content, usage = self.provider.generate(system_prompt, user_prompt, temperature)
        result = self._parse_json_response(content)
        
        return {
            "success": True,
            "content_type": "video_script",
            "script": result,
            "ai_model_used": f"{self.provider_name}/{self.provider.model}",
            "tokens_used": usage,
            "generation_time_seconds": round(time.time() - start_time, 2)
        }


# Convenience function for quick generation
async def quick_generate(
    content_type: str,
    brand_context: str,
    params: Dict[str, Any],
    provider: str = "openai"
) -> Dict[str, Any]:
    """Quick generation helper"""
    
    generator = TextGenerator(provider=provider)
    
    type_handlers = {
        "social_facebook": lambda: generator.generate_social_content(
            brand_context=brand_context,
            platform="facebook",
            **params
        ),
        "social_instagram": lambda: generator.generate_social_content(
            brand_context=brand_context,
            platform="instagram",
            **params
        ),
        "social_tiktok": lambda: generator.generate_social_content(
            brand_context=brand_context,
            platform="tiktok",
            **params
        ),
        "social_linkedin": lambda: generator.generate_social_content(
            brand_context=brand_context,
            platform="linkedin",
            **params
        ),
        "ads_facebook": lambda: generator.generate_ads_copy(
            brand_context=brand_context,
            platform="facebook",
            **params
        ),
        "ads_google": lambda: generator.generate_ads_copy(
            brand_context=brand_context,
            platform="google",
            **params
        ),
        "landing_page": lambda: generator.generate_landing_page(
            brand_context=brand_context,
            **params
        ),
        "video_script": lambda: generator.generate_video_script(
            brand_context=brand_context,
            **params
        ),
    }
    
    handler = type_handlers.get(content_type)
    if not handler:
        raise ValueError(f"Unknown content type: {content_type}")
    
    return handler()
