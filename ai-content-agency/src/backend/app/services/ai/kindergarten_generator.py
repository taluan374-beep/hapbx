"""
Kindergarten Content Generator
Specialized for Preschool/Kindergarten industry
"""
import json
from typing import Dict, Any, Optional, List
from .text_generator import TextGenerator


class KindergartenGenerator:
    """Specialized content generator for kindergarten/preschool"""
    
    def __init__(self, provider: str = "openai"):
        self.generator = TextGenerator(provider=provider)
        self.industry = "kindergarten"
    
    def _get_school_context(self, school_data: Dict) -> str:
        """Build school-specific context"""
        return f"""
## THÔNG TIN TRƯỜNG
- Tên trường: {school_data.get('name', 'Trường Mầm Non')}
- Slogan: {school_data.get('slogan', '')}
- Phương pháp giáo dục: {school_data.get('teaching_method', 'Kết hợp')}
- Độ tuổi nhận: {school_data.get('age_range', '18 tháng - 6 tuổi')}
- Địa chỉ: {school_data.get('location', '')}
- USP: {school_data.get('usp', '')}

## ĐỐI TƯỢNG: Phụ huynh có con 1-6 tuổi
- Quan tâm: Sự phát triển toàn diện, an toàn, môi trường học tập
- Pain points: Lo lắng khi gửi con, muốn biết con học gì mỗi ngày
- Mong muốn: Con vui vẻ, phát triển tốt, được quan tâm

## TONE OF VOICE
- Thân thiện, ấm áp như người thân
- Chuyên nghiệp nhưng không cứng nhắc
- Tích cực, truyền cảm hứng
- Đáng tin cậy, minh bạch

## QUY TẮC
1. Gọi học sinh: "các bé", "các con", "những thiên thần nhỏ"
2. Gọi phụ huynh: "Ba Mẹ", "Quý phụ huynh"
3. Emoji phù hợp: 🎒 📚 🌈 ⭐ 🎨 🎵 💕 🏫
4. Không dùng từ ngữ tiêu cực về trẻ
5. Luôn nhấn mạnh AN TOÀN và CHĂM SÓC
6. Hashtags: #{school_data.get('hashtag', 'MamNon')} #GiaoDucMamNon #TruongMamNon
"""

    def generate_daily_activity(
        self,
        school_data: Dict,
        activity_type: str,
        activity_details: str,
        class_name: Optional[str] = None,
        weekly_theme: Optional[str] = None,
        num_variations: int = 3
    ) -> Dict[str, Any]:
        """Generate daily activity posts"""
        
        system_prompt = f"""Bạn là Content Creator chuyên nghiệp cho ngành GIÁO DỤC MẦM NON.
{self._get_school_context(school_data)}"""

        user_prompt = f"""
## NHIỆM VỤ
Tạo {num_variations} bài post Facebook về HOẠT ĐỘNG HÀNG NGÀY.

## THÔNG TIN
- Loại hoạt động: {activity_type}
- Chi tiết: {activity_details}
- Lớp: {class_name or 'Không cụ thể'}
- Chủ đề tuần: {weekly_theme or 'Không cụ thể'}

## YÊU CẦU
Mỗi bài post gồm:
1. Hook: Mở đầu thân thiện, gợi cảm xúc
2. Body: Mô tả hoạt động, highlight điểm đặc biệt
3. Educational value: Bé học được gì
4. CTA: Mời phụ huynh tương tác
5. Hashtags: 5-7 tags phù hợp
6. Image suggestion: Gợi ý hình ảnh (không mô tả mặt trẻ)

## OUTPUT FORMAT (JSON)
```json
{{
  "posts": [
    {{
      "hook": "...",
      "body": "...",
      "educational_value": "...",
      "cta": "...",
      "hashtags": ["#tag1", "#tag2"],
      "image_suggestion": "..."
    }}
  ]
}}
```
"""
        
        content, usage = self.generator.provider.generate(system_prompt, user_prompt)
        result = self.generator._parse_json_response(content)
        
        return {
            "success": True,
            "content_type": "daily_activity",
            "activity_type": activity_type,
            "posts": result.get("posts", []),
            "tokens_used": usage
        }

    def generate_event_announcement(
        self,
        school_data: Dict,
        event_name: str,
        event_type: str,
        event_date: str,
        event_details: str,
        parent_requirements: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate event announcement posts"""
        
        system_prompt = f"""Bạn là Content Creator chuyên nghiệp cho ngành GIÁO DỤC MẦM NON.
{self._get_school_context(school_data)}"""

        user_prompt = f"""
## NHIỆM VỤ
Tạo bài post THÔNG BÁO SỰ KIỆN cho trường mầm non.

## THÔNG TIN SỰ KIỆN
- Tên sự kiện: {event_name}
- Loại: {event_type}
- Thời gian: {event_date}
- Chi tiết: {event_details}
- Yêu cầu phụ huynh: {parent_requirements or 'Không có yêu cầu đặc biệt'}

## TẠO 3 LOẠI POST:

1. **Announcement** (Trước sự kiện 1-2 tuần):
- Thông báo chi tiết 5W1H
- Highlight những điều thú vị
- Checklist cho phụ huynh
- CTA đăng ký/xác nhận

2. **Reminder** (Trước 1-2 ngày):
- Nhắc nhở ngắn gọn
- Lưu ý quan trọng
- Countdown excitement

3. **Recap** (Sau sự kiện):
- Highlight moments
- Cảm ơn
- Teaser sự kiện tiếp theo

## OUTPUT FORMAT (JSON)
```json
{{
  "announcement": {{
    "hook": "...",
    "body": "...",
    "checklist": ["...", "..."],
    "cta": "...",
    "hashtags": ["..."]
  }},
  "reminder": {{
    "content": "..."
  }},
  "recap": {{
    "content": "..."
  }}
}}
```
"""
        
        content, usage = self.generator.provider.generate(system_prompt, user_prompt)
        result = self.generator._parse_json_response(content)
        
        return {
            "success": True,
            "content_type": "event_announcement",
            "event_name": event_name,
            "posts": result,
            "tokens_used": usage
        }

    def generate_parenting_tips(
        self,
        school_data: Dict,
        topic: str,
        age_group: str = "3-6 tuổi",
        detail_level: str = "medium"  # quick_tip, medium, detailed
    ) -> Dict[str, Any]:
        """Generate parenting tips content"""
        
        system_prompt = f"""Bạn là chuyên gia giáo dục mầm non với 15+ năm kinh nghiệm.
{self._get_school_context(school_data)}

Bạn chia sẻ kiến thức nuôi dạy con một cách dễ hiểu, thực tế và có thể áp dụng ngay."""

        detail_guides = {
            "quick_tip": "1 tips ngắn gọn, dễ nhớ, dễ làm (3-5 bullets)",
            "medium": "Bài chia sẻ vừa phải với 4-6 bước cụ thể",
            "detailed": "Hướng dẫn chi tiết với lý thuyết và thực hành (carousel 5-7 slides)"
        }

        user_prompt = f"""
## NHIỆM VỤ
Tạo bài chia sẻ KIẾN THỨC NUÔI DẠY CON.

## THÔNG TIN
- Chủ đề: {topic}
- Độ tuổi: {age_group}
- Mức độ: {detail_guides.get(detail_level, detail_guides['medium'])}

## YÊU CẦU
1. Dựa trên kiến thức khoa học về phát triển trẻ
2. Thực tế, có thể áp dụng tại nhà
3. Không phán xét phụ huynh
4. Khuyến khích, động viên
5. Gợi ý hoạt động cụ thể

## OUTPUT FORMAT (JSON)
```json
{{
  "post": {{
    "type": "quick_tip/standard/carousel",
    "hook": "...",
    "main_content": "...",
    "key_points": ["...", "..."],
    "actionable_tips": ["...", "..."],
    "cta": "...",
    "hashtags": ["..."],
    "carousel_slides": ["Slide 1", "Slide 2"] // nếu là carousel
  }}
}}
```
"""
        
        content, usage = self.generator.provider.generate(system_prompt, user_prompt)
        result = self.generator._parse_json_response(content)
        
        return {
            "success": True,
            "content_type": "parenting_tips",
            "topic": topic,
            "post": result.get("post", {}),
            "tokens_used": usage
        }

    def generate_enrollment_campaign(
        self,
        school_data: Dict,
        school_year: str,
        promotion: Optional[str] = None,
        deadline: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate enrollment/admission campaign content"""
        
        system_prompt = f"""Bạn là Marketing Manager cho trường mầm non với kinh nghiệm tuyển sinh.
{self._get_school_context(school_data)}"""

        user_prompt = f"""
## NHIỆM VỤ
Tạo content cho CHIẾN DỊCH TUYỂN SINH năm học {school_year}.

## THÔNG TIN
- Năm học: {school_year}
- Ưu đãi: {promotion or 'Không có ưu đãi cụ thể'}
- Deadline: {deadline or 'Không có deadline cụ thể'}

## TẠO CONTENT THEO FUNNEL:

### 1. AWARENESS (3 posts)
- Giới thiệu trường
- Phương pháp giáo dục
- Cơ sở vật chất
- Đội ngũ giáo viên

### 2. CONSIDERATION (3 posts)
- Testimonials phụ huynh
- So sánh ưu điểm
- Câu chuyện thành công

### 3. DECISION (2 posts)
- Ưu đãi tuyển sinh
- Call to action mạnh
- Urgency/Scarcity

### FACEBOOK ADS (3 variations)
- Headlines (5 cái)
- Primary texts (3 versions)
- Descriptions (3 cái)

## OUTPUT FORMAT (JSON)
```json
{{
  "awareness_posts": [...],
  "consideration_posts": [...],
  "decision_posts": [...],
  "facebook_ads": {{
    "headlines": ["..."],
    "primary_texts": {{
      "short": "...",
      "medium": "...",
      "long": "..."
    }},
    "descriptions": ["..."]
  }},
  "landing_page": {{
    "hero_headline": "...",
    "hero_subheadline": "...",
    "benefits": ["..."],
    "cta": "..."
  }}
}}
```
"""
        
        content, usage = self.generator.provider.generate(system_prompt, user_prompt)
        result = self.generator._parse_json_response(content)
        
        return {
            "success": True,
            "content_type": "enrollment_campaign",
            "school_year": school_year,
            "campaign_content": result,
            "tokens_used": usage
        }

    def generate_video_script(
        self,
        school_data: Dict,
        video_type: str,  # tour, daily_life, teacher_intro, testimonial
        duration: int = 60,
        topic: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate video scripts for kindergarten"""
        
        system_prompt = f"""Bạn là Video Script Writer cho ngành giáo dục mầm non.
{self._get_school_context(school_data)}"""

        video_descriptions = {
            "tour": "Video giới thiệu tour trường, cơ sở vật chất",
            "daily_life": "Video một ngày của bé tại trường",
            "teacher_intro": "Video giới thiệu cô giáo",
            "testimonial": "Video phụ huynh chia sẻ",
            "activity": "Video highlight hoạt động đặc biệt"
        }

        user_prompt = f"""
## NHIỆM VỤ
Viết script video {duration} giây.

## THÔNG TIN
- Loại video: {video_type} - {video_descriptions.get(video_type, '')}
- Duration: {duration} giây
- Chủ đề cụ thể: {topic or 'Không cụ thể'}

## YÊU CẦU
1. Hook mạnh trong 3 giây đầu
2. Pacing phù hợp với duration
3. Warm, friendly tone
4. Clear CTA ở cuối
5. Gợi ý visual không bao gồm close-up mặt trẻ

## OUTPUT FORMAT (JSON)
```json
{{
  "script": {{
    "concept": "Mô tả concept",
    "total_duration": {duration},
    "segments": [
      {{
        "timestamp": "0-3s",
        "segment_type": "hook",
        "voiceover": "...",
        "visual": "...",
        "text_overlay": "...",
        "music_note": "..."
      }}
    ],
    "thumbnail_suggestion": "...",
    "caption": "Caption khi đăng video",
    "hashtags": ["..."]
  }}
}}
```
"""
        
        content, usage = self.generator.provider.generate(system_prompt, user_prompt)
        result = self.generator._parse_json_response(content)
        
        return {
            "success": True,
            "content_type": "video_script",
            "video_type": video_type,
            "script": result.get("script", {}),
            "tokens_used": usage
        }

    def generate_weekly_menu(
        self,
        school_data: Dict,
        week_start_date: str
    ) -> Dict[str, Any]:
        """Generate weekly menu announcement"""
        
        system_prompt = f"""Bạn là Content Creator cho trường mầm non.
{self._get_school_context(school_data)}"""

        user_prompt = f"""
## NHIỆM VỤ
Tạo bài post THỰC ĐƠN TUẦN cho trường mầm non.

## THÔNG TIN
- Tuần bắt đầu: {week_start_date}

## YÊU CẦU
1. Format đẹp, dễ đọc
2. Highlight dinh dưỡng
3. Gợi ý thực đơn cân bằng 4 nhóm chất
4. Thân thiện với phụ huynh

## OUTPUT FORMAT (JSON)
```json
{{
  "menu_post": {{
    "hook": "...",
    "menu": {{
      "monday": {{
        "breakfast": "...",
        "lunch": "...",
        "snack": "..."
      }},
      "tuesday": {{...}},
      "wednesday": {{...}},
      "thursday": {{...}},
      "friday": {{...}}
    }},
    "nutrition_note": "Ghi chú về dinh dưỡng",
    "cta": "...",
    "hashtags": ["..."]
  }}
}}
```
"""
        
        content, usage = self.generator.provider.generate(system_prompt, user_prompt)
        result = self.generator._parse_json_response(content)
        
        return {
            "success": True,
            "content_type": "weekly_menu",
            "week": week_start_date,
            "menu_post": result.get("menu_post", {}),
            "tokens_used": usage
        }


# Quick generation functions
async def generate_kindergarten_content(
    content_type: str,
    school_data: Dict,
    params: Dict,
    provider: str = "openai"
) -> Dict[str, Any]:
    """
    Quick function to generate kindergarten content
    
    content_types:
    - daily_activity
    - event_announcement
    - parenting_tips
    - enrollment_campaign
    - video_script
    - weekly_menu
    """
    
    generator = KindergartenGenerator(provider=provider)
    
    handlers = {
        "daily_activity": lambda: generator.generate_daily_activity(school_data, **params),
        "event_announcement": lambda: generator.generate_event_announcement(school_data, **params),
        "parenting_tips": lambda: generator.generate_parenting_tips(school_data, **params),
        "enrollment_campaign": lambda: generator.generate_enrollment_campaign(school_data, **params),
        "video_script": lambda: generator.generate_video_script(school_data, **params),
        "weekly_menu": lambda: generator.generate_weekly_menu(school_data, **params),
    }
    
    handler = handlers.get(content_type)
    if not handler:
        raise ValueError(f"Unknown content type: {content_type}")
    
    return handler()
