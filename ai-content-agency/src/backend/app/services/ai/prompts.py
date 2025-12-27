"""
Prompt Templates & Builder
"""
from typing import Dict, Any, Optional


class PromptBuilder:
    """Build prompts for different content types"""
    
    @staticmethod
    def get_system_prompt(brand_context: str) -> str:
        """Base system prompt with brand context"""
        return f"""Bạn là một Content Strategist và Copywriter chuyên nghiệp với 10+ năm kinh nghiệm.
Bạn tạo content marketing chất lượng cao, sáng tạo và phù hợp với thương hiệu.

{brand_context}

## QUY TẮC QUAN TRỌNG
1. Output phải bằng Tiếng Việt (trừ khi yêu cầu khác)
2. Giữ đúng tone of voice của thương hiệu
3. Tập trung vào BENEFIT, không chỉ feature
4. Luôn có CTA rõ ràng
5. Format output theo JSON đã quy định
6. KHÔNG bịa đặt thông tin sản phẩm - chỉ dùng thông tin được cung cấp
7. Sáng tạo trong cách diễn đạt nhưng chính xác về nội dung
"""

    @staticmethod
    def get_social_prompt(
        platform: str,
        objective: str,
        topic: str,
        product_name: Optional[str] = None,
        key_message: Optional[str] = None,
        promotion: Optional[str] = None,
        body_length: str = "medium",
        num_variations: int = 3
    ) -> str:
        """Prompt for social media content"""
        
        length_guide = {
            "short": "2-3 câu ngắn gọn",
            "medium": "4-6 câu, có storytelling nhẹ",
            "long": "7-10 câu, storytelling chi tiết"
        }
        
        platform_guides = {
            "facebook": """
- Dòng đầu tiên (hook) phải gây tò mò, khiến người đọc dừng scroll
- Có thể dùng emoji nhưng không quá 3 cái
- CTA rõ ràng: comment, inbox, click link
- Hashtags: 3-5 tags phù hợp""",
            "instagram": """
- Hook phải nằm trong 125 ký tự đầu (trước "more")
- Visual-first: Caption hỗ trợ hình ảnh
- Hashtags: 15-20 tags, mix branded + niche + popular
- Gợi ý concept hình ảnh đi kèm""",
            "tiktok": """
- Hook cực ngắn và viral (5-10 từ)
- Trend-aware language
- Hashtags: 5-7 tags trending + niche
- Suggest trending audio nếu phù hợp""",
            "linkedin": """
- Professional tone
- Thought leadership angle
- Storytelling cá nhân hoạt động tốt
- Hashtags: 3-5 tags ngành nghề"""
        }
        
        return f"""## NHIỆM VỤ
Tạo {num_variations} bài post {platform.upper()} cho thương hiệu.

## THÔNG TIN
- Chủ đề: {topic}
- Sản phẩm liên quan: {product_name or 'Không cụ thể'}
- Mục tiêu: {objective}
- Thông điệp chính: {key_message or 'Không cụ thể'}
- Promotion: {promotion or 'Không có'}

## YÊU CẦU PLATFORM ({platform.upper()})
{platform_guides.get(platform, platform_guides['facebook'])}

## BODY LENGTH
{length_guide.get(body_length, length_guide['medium'])}

## OUTPUT FORMAT (JSON)
```json
{{
  "variations": [
    {{
      "hook": "Dòng đầu tiên gây chú ý",
      "body": "Nội dung chính với xuống dòng hợp lý",
      "cta": "Kêu gọi hành động",
      "hashtags": ["#tag1", "#tag2", "#tag3"],
      "image_suggestion": "Gợi ý hình ảnh đi kèm",
      "best_posting_time": "Thời gian đăng tốt nhất"
    }}
  ]
}}
```

Tạo {num_variations} variations khác nhau về góc nhìn và cách tiếp cận.
"""

    @staticmethod
    def get_ads_prompt(
        platform: str,
        product_name: str,
        offer: Optional[str] = None,
        landing_url: Optional[str] = None,
        objective: str = "conversion",
        num_variations: int = 3
    ) -> str:
        """Prompt for ads copy"""
        
        platform_specs = {
            "facebook": """
## FACEBOOK/INSTAGRAM ADS FORMAT
- Primary Text: 3 versions (short/medium/long)
- Headlines: 5 versions (max 40 ký tự)
- Descriptions: 3 versions (max 125 ký tự)
- CTA Button: Shop Now / Learn More / Sign Up / Get Offer""",
            "google": """
## GOOGLE SEARCH ADS FORMAT
- Headlines: 15 cái (max 30 ký tự mỗi cái)
  - 5 keyword-focused
  - 5 benefit-focused
  - 3 CTA/offer
  - 2 trust signals
- Descriptions: 4 cái (max 90 ký tự mỗi cái)""",
            "tiktok": """
## TIKTOK ADS FORMAT
- Hook: 3 variations (5-10 từ, gây chú ý ngay)
- Primary Text: 3 versions
- CTA: Link in bio style"""
        }
        
        return f"""## NHIỆM VỤ
Tạo ads copy cho {platform.upper()} campaign.

## THÔNG TIN CAMPAIGN
- Sản phẩm: {product_name}
- Offer: {offer or 'Không có offer cụ thể'}
- Landing URL: {landing_url or 'N/A'}
- Mục tiêu: {objective}

{platform_specs.get(platform, platform_specs['facebook'])}

## COPYWRITING FRAMEWORKS (Áp dụng đa dạng)
1. AIDA: Attention → Interest → Desire → Action
2. PAS: Problem → Agitate → Solution
3. BAB: Before → After → Bridge

## OUTPUT FORMAT (JSON)
```json
{{
  "variations": [
    {{
      "variation_name": "V1 - [Framework used]",
      "primary_text": {{
        "short": "1-2 câu",
        "medium": "3-4 câu",
        "long": "5-7 câu với storytelling"
      }},
      "headlines": ["Headline 1", "Headline 2", "..."],
      "descriptions": ["Desc 1", "Desc 2", "Desc 3"],
      "cta_button": "Shop Now",
      "hook": "Dòng đầu tiên gây chú ý nhất",
      "image_direction": "Gợi ý visual cho ad"
    }}
  ],
  "a_b_test_recommendation": "Gợi ý A/B test"
}}
```

Tạo {num_variations} variations với các framework khác nhau.
"""

    @staticmethod
    def get_landing_page_prompt(
        product_name: str,
        price: Optional[str] = None,
        offer: Optional[str] = None,
        page_type: str = "sales"  # sales, lead_gen
    ) -> str:
        """Prompt for landing page copy"""
        
        return f"""## NHIỆM VỤ
Viết copy hoàn chỉnh cho Landing Page {page_type}.

## THÔNG TIN SẢN PHẨM
- Tên: {product_name}
- Giá: {price or 'Liên hệ'}
- Offer: {offer or 'Không có'}

## CẤU TRÚC LANDING PAGE

### Section 1: HERO
- Headline: USP chính (6-12 từ, impactful)
- Subheadline: Mở rộng headline (15-25 từ)
- CTA Button text

### Section 2: PROBLEM (3-4 pain points)
- Emotional triggers
- Relatable situations

### Section 3: SOLUTION
- Giới thiệu sản phẩm
- How it works (3 bước)
- Key differentiators

### Section 4: FEATURES & BENEFITS (4-6 items)
- Mỗi feature: Icon suggestion + Tên + Benefit

### Section 5: SOCIAL PROOF
- 3 testimonial templates
- Trust badges
- Stats/Numbers

### Section 6: PRICING/OFFER
- Price presentation
- What's included
- Guarantee

### Section 7: FAQ (5-7 câu)
- Objection handling

### Section 8: FINAL CTA
- Urgency element
- Risk reversal

## OUTPUT FORMAT (JSON)
```json
{{
  "hero": {{
    "headline": "...",
    "subheadline": "...",
    "cta_button": "...",
    "image_direction": "..."
  }},
  "problem": {{
    "section_headline": "...",
    "pain_points": [
      {{"emoji": "😫", "text": "Pain point 1"}},
      {{"emoji": "😤", "text": "Pain point 2"}}
    ]
  }},
  "solution": {{
    "intro": "...",
    "how_it_works": [
      {{"step": 1, "title": "...", "description": "..."}},
      {{"step": 2, "title": "...", "description": "..."}},
      {{"step": 3, "title": "...", "description": "..."}}
    ]
  }},
  "features": [
    {{"icon": "⚡", "name": "...", "benefit": "..."}}
  ],
  "social_proof": {{
    "testimonials": [
      {{"quote": "...", "name": "...", "title": "...", "result": "..."}}
    ],
    "stats": [
      {{"number": "10,000+", "label": "Khách hàng"}}
    ]
  }},
  "pricing": {{
    "original_price": "...",
    "sale_price": "...",
    "includes": ["..."],
    "guarantee": "..."
  }},
  "faq": [
    {{"question": "...", "answer": "..."}}
  ],
  "final_cta": {{
    "headline": "...",
    "urgency": "...",
    "cta_button": "..."
  }}
}}
```
"""

    @staticmethod
    def get_video_script_prompt(
        platform: str,
        duration: int,
        topic: str,
        product_name: Optional[str] = None,
        video_style: str = "talking_head"
    ) -> str:
        """Prompt for video script"""
        
        style_guides = {
            "talking_head": "Người nói trực tiếp vào camera",
            "voiceover": "Voiceover + B-roll footage",
            "text_overlay": "Text trên màn hình + nhạc background",
            "tutorial": "Hướng dẫn step-by-step với demo"
        }
        
        structure_by_duration = {
            15: """[0-2s] HOOK - Gây chú ý ngay
[2-12s] CONTENT - Nội dung chính, đi thẳng vào vấn đề
[12-15s] CTA - Kêu gọi hành động""",
            30: """[0-3s] HOOK - Pattern interrupt, gây tò mò
[3-10s] PROBLEM - Nêu vấn đề/pain point
[10-22s] SOLUTION - Giải pháp/nội dung chính
[22-27s] PROOF - Social proof hoặc demo
[27-30s] CTA - Kêu gọi hành động""",
            60: """[0-3s] HOOK - Mạnh mẽ, gây shock hoặc tò mò
[3-12s] PROBLEM - Setup vấn đề
[12-40s] SOLUTION - Nội dung chính, có thể chia 3-5 points
[40-52s] PROOF - Kết quả, transformation
[52-60s] CTA - Call to action rõ ràng"""
        }
        
        return f"""## NHIỆM VỤ
Viết script video {platform.upper()} {duration} giây.

## THÔNG TIN
- Chủ đề: {topic}
- Sản phẩm: {product_name or 'Không cụ thể'}
- Style: {video_style} ({style_guides.get(video_style, 'N/A')})
- Duration: {duration} giây

## CẤU TRÚC SCRIPT
{structure_by_duration.get(duration, structure_by_duration[30])}

## HOOK FORMULAS (Chọn phù hợp)
1. "POV: [tình huống]"
2. "Bạn có biết [fact gây shock]?"
3. "Đừng [hành động] cho đến khi xem hết video này"
4. "[Number] điều về [topic] không ai nói"
5. "Nếu bạn [vấn đề], đây là dành cho bạn"

## OUTPUT FORMAT (JSON)
```json
{{
  "concept": "Mô tả ngắn concept video",
  "total_duration": {duration},
  "segments": [
    {{
      "timestamp": "0-3s",
      "type": "hook",
      "spoken_text": "Text người nói/voiceover",
      "text_overlay": "Text hiển thị trên màn hình",
      "visual": "Mô tả hình ảnh/hành động",
      "audio_note": "Ghi chú về âm thanh/nhạc"
    }}
  ],
  "caption": "Caption cho video khi đăng",
  "hashtags": ["#tag1", "#tag2"],
  "hook_variations": ["Hook alt 1", "Hook alt 2"],
  "thumbnail_suggestion": "Gợi ý thumbnail"
}}
```
"""


# Industry-specific example templates
INDUSTRY_EXAMPLES = {
    "beauty": {
        "social_facebook": """
### Ví dụ ngành Beauty:
Hook: "Bạn đang dùng serum sai cách mà không biết 😱"
Body: "90% chị em apply serum khi da còn ướt - và đó là SAI!

Da ướt = serum bị pha loãng = giảm 50% hiệu quả.

Cách đúng:
✓ Sau rửa mặt, thấm khô nhẹ (da còn ẩm, không ướt)
✓ Apply serum khi da còn ẩm
✓ Đợi 30s rồi mới thoa kem dưỡng

Thử ngay và cảm nhận sự khác biệt!"
CTA: "Save lại và tag người hay skincare sai cách nhé!"
""",
    },
    "fnb": {
        "social_facebook": """
### Ví dụ ngành F&B:
Hook: "Team cà phê đen hay cà phê sữa? ☕"
Body: "Mỗi buổi sáng, 10 người ghé quán thì 7 người gọi cà phê sữa.

Nhưng team cà phê đen tuy ít mà 'chất' - một khi đã ghiền thì loyal vô cùng!

Còn bạn thuộc team nào?"
CTA: "Comment team của bạn và tag bạn cafe cùng nhé! 👇"
""",
    },
    "education": {
        "social_facebook": """
### Ví dụ ngành Education:
Hook: "Học tiếng Anh 10 năm vẫn không nói được - Đây là lý do 🤯"
Body: "Bạn biết grammar, biết vocabulary, đọc hiểu tốt...

Nhưng khi cần nói thì... đơ!

Lý do: Não bạn đang 'dịch' thay vì 'phản xạ'.

3 cách fix:
1️⃣ Shadowing - Nghe và nhại theo ngay lập tức
2️⃣ Self-talk - Nói chuyện với chính mình bằng tiếng Anh
3️⃣ Spaced repetition - Ôn lại đúng thời điểm não sắp quên"
CTA: "Bạn đang mắc lỗi nào? Comment chia sẻ nhé!"
""",
    }
}
