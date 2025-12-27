# 📝 PHẦN 2: PROMPT TEMPLATES CHI TIẾT

## Cấu trúc Prompt Engineering

```
┌─────────────────────────────────────────────────────┐
│              SYSTEM PROMPT (Brand DNA)              │
│  • Role definition                                  │
│  • Brand context                                    │
│  • Tone & Style guidelines                          │
│  • Output constraints                               │
└─────────────────────────────────────────────────────┘
                        +
┌─────────────────────────────────────────────────────┐
│              USER PROMPT (Task Specific)            │
│  • Specific request                                 │
│  • Parameters                                       │
│  • Examples (few-shot)                              │
│  • Output format                                    │
└─────────────────────────────────────────────────────┘
                        =
┌─────────────────────────────────────────────────────┐
│              OPTIMIZED OUTPUT                       │
│  • Consistent brand voice                           │
│  • Structured format                                │
│  • Ready to use                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🏢 BASE SYSTEM PROMPT (Dùng cho tất cả)

```python
BASE_SYSTEM_PROMPT = """
Bạn là một Content Strategist và Copywriter chuyên nghiệp với 10+ năm kinh nghiệm trong ngành {industry}.

## BRAND CONTEXT
- Tên thương hiệu: {brand_name}
- Ngành: {industry}
- USP (Điểm bán hàng độc nhất): {usp}
- Giá trị cốt lõi: {core_values}

## KHÁCH HÀNG MỤC TIÊU
- Độ tuổi: {age_range}
- Giới tính: {gender}
- Vị trí: {location}
- Thu nhập: {income_level}
- Pain points chính: {pain_points}
- Mong muốn: {desires}

## TONE OF VOICE
- Style: {tone_style} 
  (Options: professional, friendly, playful, luxury, casual, authoritative)
- Ngôn ngữ: {language_style}
  (Options: formal, conversational, trendy, simple)
- Cảm xúc: {emotional_tone}
  (Options: inspiring, reassuring, exciting, calm, urgent)

## QUY TẮC QUAN TRỌNG
1. KHÔNG sử dụng các từ: {banned_words}
2. LUÔN đề cập: {must_mention}
3. Độ dài tối đa: {max_length}
4. Ngôn ngữ: Tiếng Việt (trừ khi yêu cầu khác)
5. KHÔNG dùng emoji quá 3 cái/bài (trừ khi brand cho phép)
"""
```

---

## 📱 1. SOCIAL MEDIA CONTENT PROMPTS

### 1.1 Facebook Post

```python
FACEBOOK_POST_PROMPT = """
## NHIỆM VỤ
Tạo {number} bài post Facebook cho thương hiệu.

## YÊU CẦU NỘI DUNG
- Mục tiêu: {objective}
  • awareness: Tăng nhận diện thương hiệu
  • engagement: Tăng tương tác (like, comment, share)
  • conversion: Thúc đẩy hành động (mua hàng, đăng ký)
  • traffic: Tăng traffic về website

- Chủ đề: {topic}
- Sản phẩm/Dịch vụ liên quan: {product_service}
- Thông điệp chính: {key_message}
- Promotion (nếu có): {promotion}

## CẤU TRÚC BÀI POST
1. **HOOK** (Dòng đầu tiên - QUAN TRỌNG NHẤT)
   - Gây tò mò, gây shock, hoặc nêu vấn đề
   - Phải khiến người đọc dừng scroll
   - Tối đa 10-15 từ

2. **BODY** (Nội dung chính)
   - Triển khai ý tưởng
   - Nêu lợi ích, không chỉ tính năng
   - Storytelling nếu phù hợp
   - Độ dài: {body_length} (short: 2-3 câu, medium: 4-6 câu, long: 7-10 câu)

3. **CTA** (Kêu gọi hành động)
   - Rõ ràng, cụ thể
   - Tạo urgency nếu phù hợp
   - Ví dụ: "Comment ngay", "Inbox để nhận ưu đãi", "Click link trong bio"

4. **HASHTAGS** (5-10 tags)
   - 2-3 branded hashtags
   - 3-4 industry hashtags
   - 2-3 trending/popular hashtags

## OUTPUT FORMAT (JSON)
```json
{
  "posts": [
    {
      "hook": "...",
      "body": "...",
      "cta": "...",
      "hashtags": ["#tag1", "#tag2"],
      "best_posting_time": "...",
      "image_suggestion": "...",
      "estimated_engagement": "high/medium/low"
    }
  ]
}
```

## VÍ DỤ TỐT (Few-shot)
{few_shot_examples}
"""

# Few-shot examples cho ngành F&B
FB_FNB_EXAMPLES = """
### Ví dụ 1 (Engagement post):
Hook: "Bạn thuộc team cà phê đen hay cà phê sữa? ☕"
Body: "Mình thấy dân văn phòng 10 người thì 7 người chọn cà phê sữa vì vị ngọt dễ uống. Còn team cà phê đen thì ít nhưng toàn 'chân ái' - một khi đã ghiền thì không đổi được! Bạn thì sao?"
CTA: "Comment team của bạn và tag người bạn hay uống cà phê cùng nhé!"
Hashtags: #CoffeeLover #TeamCaPhe #CaPheVietNam #MorningCoffee

### Ví dụ 2 (Conversion post):
Hook: "FLASH SALE 3 TIẾNG - Giảm 30% toàn menu! ⚡"
Body: "Chỉ từ 14h-17h hôm nay, tất cả đồ uống tại {brand_name} đều giảm 30%! Trà sữa size L chỉ còn 35k, Cà phê đặc biệt chỉ 28k. Số lượng có hạn theo khung giờ!"
CTA: "Đặt ngay trên app hoặc Grab/ShopeeFood để không bỏ lỡ!"
Hashtags: #FlashSale #GiamGia30 #TraSua #CaPhe #UongGi
"""
```

### 1.2 Instagram Post

```python
INSTAGRAM_POST_PROMPT = """
## NHIỆM VỤ
Tạo {number} caption Instagram cho thương hiệu.

## ĐẶC THÙ INSTAGRAM
- Visual-first: Caption hỗ trợ hình ảnh, không thay thế
- Shorter attention span: Hook phải cực mạnh
- Hashtag strategy quan trọng hơn Facebook
- Stories-friendly: Có thể tạo poll/quiz

## YÊU CẦU
- Loại post: {post_type}
  • feed: Post chính trên feed
  • carousel: Nhiều ảnh (tạo caption cho từng slide concept)
  • reel: Caption cho video ngắn
  • story: Text ngắn cho story

- Mục tiêu: {objective}
- Hình ảnh/Video mô tả: {visual_description}

## CẤU TRÚC CAPTION

### Cho Feed/Carousel:
1. **Hook** (trong 125 ký tự đầu - hiển thị trước "more")
2. **Body** (triển khai ý, xuống dòng tạo không gian)
3. **CTA** (engage or convert)
4. **Hashtag block** (comment đầu tiên hoặc cuối caption)
   - 20-30 hashtags
   - Mix: branded (3), niche (10), popular (10), location (2-5)

### Cho Reel:
1. **Hook ngắn** (5-7 từ)
2. **Context** (1-2 câu mô tả video)
3. **CTA** (follow, save, share)
4. **Hashtags** (trending + niche)

## OUTPUT FORMAT (JSON)
```json
{
  "captions": [
    {
      "hook": "...",
      "body": "...",
      "cta": "...",
      "hashtags_main": ["#tag1", "..."],
      "hashtags_comment": ["#tag1", "..."],
      "carousel_slides": ["Slide 1 concept", "Slide 2 concept"],
      "image_direction": "Mô tả hướng dẫn chụp/thiết kế ảnh"
    }
  ]
}
```
"""
```

### 1.3 TikTok/Reels Script

```python
TIKTOK_SCRIPT_PROMPT = """
## NHIỆM VỤ
Viết script video TikTok/Reels {duration} giây.

## THÔNG TIN VIDEO
- Chủ đề: {topic}
- Style: {video_style}
  • talking_head: Người nói trực tiếp vào camera
  • voiceover: Voice + B-roll footage
  • text_overlay: Text trên màn hình + nhạc
  • skit: Diễn kịch ngắn
  • tutorial: Hướng dẫn step-by-step

- Trend audio (nếu có): {trending_audio}
- Mục tiêu: {objective}

## CẤU TRÚC SCRIPT THEO THỜI GIAN

### Video 15 giây:
[0-2s] HOOK - Gây chú ý ngay lập tức
[2-10s] CONTENT - Nội dung chính, đi thẳng vào vấn đề
[10-15s] CTA - Kêu gọi hành động

### Video 30 giây:
[0-3s] HOOK - Pattern interrupt, gây tò mò
[3-8s] PROBLEM - Nêu vấn đề/pain point
[8-20s] SOLUTION - Giải pháp/nội dung chính
[20-27s] PROOF - Social proof hoặc demo
[27-30s] CTA - Follow/Like/Comment/Mua

### Video 60 giây:
[0-3s] HOOK - Mạnh mẽ, gây shock hoặc tò mò
[3-10s] CONTEXT - Setup bối cảnh
[10-35s] CONTENT - Nội dung chính, có thể chia 3-5 points
[35-50s] PROOF/TRANSFORMATION - Kết quả, before/after
[50-60s] CTA - Call to action rõ ràng

## HOOK FORMULAS (Chọn phù hợp)
1. "POV: [tình huống]" - Point of view
2. "Bạn có biết [fact gây shock]?"
3. "Đừng [hành động] cho đến khi xem hết video này"
4. "[Number] điều về [topic] mà không ai nói cho bạn"
5. "Nếu bạn [vấn đề], đây là dành cho bạn"
6. "Story time: [teaser]"
7. "Wait for it... 👀"
8. "Thử [hành động] trong [thời gian] và đây là kết quả"

## OUTPUT FORMAT (JSON)
```json
{
  "script": {
    "total_duration": 30,
    "segments": [
      {
        "timestamp": "0-3s",
        "type": "hook",
        "spoken_text": "Text người nói",
        "text_overlay": "Text hiển thị trên màn hình",
        "visual": "Mô tả hình ảnh/hành động",
        "audio_note": "Ghi chú về âm thanh/nhạc"
      },
      {
        "timestamp": "3-8s",
        "type": "problem",
        "spoken_text": "...",
        "text_overlay": "...",
        "visual": "...",
        "audio_note": "..."
      }
    ],
    "caption": "Caption cho video",
    "hashtags": ["#trending", "#niche"],
    "best_posting_time": "19:00-21:00",
    "trending_audio_suggestion": "Tên bài/sound trending phù hợp"
  }
}
```

## VÍ DỤ SCRIPT (Ngành Beauty/Skincare)
```
[0-3s] HOOK
Spoken: "3 thứ trong skincare routine của bạn đang phá hủy da!"
Visual: Close-up mặt với expression shock
Text overlay: "STOP DOING THIS ❌"

[3-10s] PROBLEM  
Spoken: "Số 1: Rửa mặt bằng nước nóng. Nước nóng làm mất độ ẩm tự nhiên và khiến da tiết dầu nhiều hơn."
Visual: Demo rửa mặt nước nóng, then nước ấm
Text overlay: "❌ Nước nóng → ✅ Nước ấm"

[10-20s] SOLUTION
Spoken: "Số 2: Dùng quá nhiều sản phẩm. Da bạn không cần 10 bước, chỉ cần 4 bước đúng..."
Visual: So sánh 10 products vs 4 products
Text overlay: "Less is more 💫"

[20-27s] PROOF
Spoken: "Đây là kết quả sau 2 tuần mình đổi routine"
Visual: Before/After transformation
Text overlay: "2 weeks later ✨"

[27-30s] CTA
Spoken: "Save video này và follow để xem routine 4 bước chi tiết!"
Visual: Point to follow button
Text overlay: "SAVE + FOLLOW 👆"
```
"""
```

### 1.4 LinkedIn Post (B2B)

```python
LINKEDIN_POST_PROMPT = """
## NHIỆM VỤ
Tạo {number} bài post LinkedIn chuyên nghiệp.

## ĐẶC THÙ LINKEDIN
- Professional tone
- Thought leadership content
- Storytelling cá nhân hoạt động tốt
- Longer content OK (nhưng hook vẫn quan trọng)
- Comment section = networking

## LOẠI POST
- {post_type}:
  • thought_leadership: Chia sẻ insight ngành
  • story: Câu chuyện cá nhân/nghề nghiệp
  • tips: Tips/advice chuyên môn
  • announcement: Thông báo công ty
  • engagement: Câu hỏi/poll tạo discussion
  • carousel: Document/PDF nhiều trang

## CẤU TRÚC BÀI POST

### Thought Leadership:
```
[Hook - Controversial/Insight statement]

[Blank line - tạo "See more"]

[Context - Vì sao bạn nghĩ vậy]

[3-5 Bullet points - Supporting arguments]

[Personal take - Quan điểm cá nhân]

[CTA - Hỏi ý kiến hoặc yêu cầu engage]
```

### Story Format:
```
[Hook - Kết quả hoặc lesson learned]

[Setup - Bối cảnh câu chuyện]

[Conflict - Khó khăn/thử thách]

[Resolution - Cách giải quyết]

[Lesson - Bài học rút ra]

[CTA - Bạn có trải nghiệm tương tự?]
```

## OUTPUT FORMAT (JSON)
```json
{
  "posts": [
    {
      "hook": "Dòng đầu tiên (hiện trước See more)",
      "body": "Nội dung chính với \\n\\n để xuống dòng",
      "cta": "Câu kêu gọi tương tác",
      "hashtags": ["#tag1", "#tag2", "#tag3"],
      "post_type": "thought_leadership",
      "best_day": "Tuesday/Wednesday/Thursday",
      "image_suggestion": "Mô tả ảnh nếu cần"
    }
  ]
}
```

## VÍ DỤ (Thought Leadership)
```
Tôi đã sa thải đội marketing 5 người và thay bằng AI.

Kết quả? Revenue tăng 40%.

Nhưng đây là điều không ai nói với bạn:

→ AI không thay thế được strategy
→ AI xuất sắc ở execution
→ Tôi vẫn cần 1 người "điều phối" AI
→ Chi phí giảm 70%, output tăng 3x

Bí mật thực sự?

Tôi không sa thải để cắt giảm.
Tôi sa thải để RE-HIRE những người có thể leverage AI.

Năm 2025, câu hỏi không còn là "AI hay người?"
Mà là "Người + AI vs Chỉ người"

Bạn đã bắt đầu adapt chưa?

#AIMarketing #FutureOfWork #ContentStrategy
```
"""
```

---

## 🎯 2. ADS COPY PROMPTS

### 2.1 Facebook/Instagram Ads

```python
FACEBOOK_ADS_PROMPT = """
## NHIỆM VỤ
Tạo {number} variations cho Facebook/Instagram Ads campaign.

## CAMPAIGN BRIEF
- Sản phẩm/Dịch vụ: {product_service}
- Giá: {price}
- Offer/Promotion: {offer}
- Landing page URL: {landing_url}
- Mục tiêu campaign: {campaign_objective}
  • awareness: Brand awareness, Reach
  • consideration: Traffic, Engagement, Video views
  • conversion: Conversions, Catalog sales, Lead gen

## TARGET AUDIENCE
- Demographics: {demographics}
- Interests: {interests}
- Pain points: {pain_points}
- Desires: {desires}

## AD FORMAT
- Format: {ad_format}
  • single_image: 1 ảnh
  • carousel: 3-10 ảnh
  • video: Video ad
  • collection: Collection ad

## YÊU CẦU COPY

### Primary Text (3 variations mỗi style):
- Short (1-2 câu): Cho mobile, quick scan
- Medium (3-4 câu): Balance
- Long (5-7 câu): Storytelling, more detail

### Headlines (5 variations):
- Benefit-focused
- Curiosity-driven
- Urgency/Scarcity
- Social proof
- Question

### Descriptions (3 variations):
- Supporting the headline
- 1 câu ngắn gọn

## COPYWRITING FRAMEWORKS

### AIDA (Attention-Interest-Desire-Action):
- A: Grab attention với hook mạnh
- I: Build interest với benefits
- D: Create desire với transformation/results
- A: Clear CTA

### PAS (Problem-Agitate-Solution):
- P: State the problem
- A: Agitate - make them feel the pain
- S: Present your solution

### BAB (Before-After-Bridge):
- Before: Current situation (pain)
- After: Dream outcome
- Bridge: Your product/service

## OUTPUT FORMAT (JSON)
```json
{
  "ad_variations": [
    {
      "variation_name": "V1 - Benefit Focus",
      "primary_text": {
        "short": "...",
        "medium": "...",
        "long": "..."
      },
      "headlines": [
        "Headline 1",
        "Headline 2",
        "Headline 3",
        "Headline 4",
        "Headline 5"
      ],
      "descriptions": [
        "Description 1",
        "Description 2",
        "Description 3"
      ],
      "cta_button": "Shop Now / Learn More / Sign Up / Get Offer",
      "framework_used": "AIDA",
      "image_direction": "Mô tả ý tưởng visual"
    }
  ],
  "a_b_test_recommendation": "Gợi ý A/B test",
  "audience_message_match": "Giải thích tại sao copy này match với audience"
}
```

## VÍ DỤ (Ngành Skincare - Conversion Campaign)

### Variation 1 - Problem-Agitate-Solution:
**Primary Text (Long):**
"Bạn đã thử đủ loại kem trị mụn mà vẫn thất bại?

Mình hiểu cảm giác đó. Tốn tiền triệu, da vẫn sần sùi, tự ti mỗi khi ra đường.

Cho đến khi mình phát hiện ra: 90% kem trị mụn chỉ trị TRIỆU CHỨNG, không trị GỐC.

{Product Name} khác biệt:
✓ Công nghệ {technology} - đi sâu vào tận gốc mụn
✓ 97% người dùng thấy kết quả trong 14 ngày
✓ Được bác sĩ da liễu khuyên dùng

🎁 Hôm nay: Giảm 30% + Free ship!"

**Headlines:**
1. "Da sạch mụn trong 14 ngày - Cam kết hoàn tiền"
2. "97% người dùng hết mụn - Bạn là người tiếp theo?"
3. "Bác sĩ da liễu khuyên dùng - Kết quả thật"
4. "Mụn dai dẳng? Đây là giải pháp cuối cùng"
5. "SALE 30% - Chỉ hôm nay"

**Descriptions:**
1. "Công nghệ {technology} độc quyền"
2. "Free ship + Quà tặng kèm"
3. "Được 50,000+ khách hàng tin dùng"
"""
```

### 2.2 Google Ads (Search)

```python
GOOGLE_SEARCH_ADS_PROMPT = """
## NHIỆM VỤ
Tạo Google Search Ads copy cho campaign.

## THÔNG TIN CAMPAIGN
- Sản phẩm/Dịch vụ: {product_service}
- Keywords mục tiêu: {target_keywords}
- Landing page: {landing_url}
- USP: {usp}
- Offer: {offer}

## GIỚI HẠN KÝ TỰ GOOGLE ADS
- Headlines: Tối đa 30 ký tự/headline (15 headlines)
- Descriptions: Tối đa 90 ký tự/description (4 descriptions)

## YÊU CẦU

### Headlines (15 cái, <30 ký tự mỗi cái):
Chia thành groups:
- Group 1 (5): Chứa keyword chính
- Group 2 (5): Benefit/USP focused
- Group 3 (3): CTA/Offer
- Group 4 (2): Trust signals

### Descriptions (4 cái, <90 ký tự mỗi cái):
- Desc 1: Benefit chính + keyword
- Desc 2: Features/What you get
- Desc 3: Social proof/Trust
- Desc 4: Offer/CTA

## OUTPUT FORMAT (JSON)
```json
{
  "responsive_search_ad": {
    "headlines": {
      "keyword_focused": [
        {"text": "...", "char_count": 25},
        {"text": "...", "char_count": 28}
      ],
      "benefit_focused": [...],
      "cta_offer": [...],
      "trust_signals": [...]
    },
    "descriptions": [
      {"text": "...", "char_count": 85},
      {"text": "...", "char_count": 88}
    ],
    "pinning_recommendation": {
      "headline_position_1": "Keyword headline",
      "headline_position_2": "Benefit headline",
      "description_position_1": "Main benefit description"
    }
  }
}
```

## VÍ DỤ (Keyword: "khóa học tiếng anh online")

**Headlines:**
1. "Khóa Học Tiếng Anh Online" (26) - keyword
2. "Học Tiếng Anh Tại Nhà" (21) - keyword
3. "Giao Tiếp Lưu Loát 3 Tháng" (25) - benefit
4. "Cam Kết Đầu Ra IELTS 6.5" (24) - benefit
5. "Học 1-1 Với Giáo Viên" (21) - feature
6. "Giảm 40% Học Phí" (17) - offer
7. "Đăng Ký Học Thử Miễn Phí" (25) - CTA
8. "50,000+ Học Viên Tin Dùng" (26) - trust

**Descriptions:**
1. "Khóa học tiếng Anh online với giáo viên bản ngữ. Cam kết giao tiếp tự tin sau 3 tháng." (88)
2. "Học mọi lúc mọi nơi. Lộ trình cá nhân hóa. App học tập thông minh. Hỗ trợ 24/7." (82)
"""
```

### 2.3 TikTok Ads Script

```python
TIKTOK_ADS_SCRIPT_PROMPT = """
## NHIỆM VỤ
Viết script cho TikTok Ads ({duration} giây).

## ĐẶC THÙ TIKTOK ADS
- Phải native, không quá "quảng cáo"
- Hook trong 1-2 giây đầu QUYẾT ĐỊNH
- Format UGC (User Generated Content) hoạt động tốt nhất
- Sound/Music quan trọng

## AD FORMATS
- {ad_format}:
  • spark_ads: Boost organic post
  • in_feed: Native in-feed video
  • top_view: First thing users see

## SCRIPT STRUCTURE FOR ADS

### Problem-Solution (Best for conversion):
[0-2s] HOOK: "Struggling with [problem]?"
[2-5s] AGITATE: Make them feel the pain
[5-15s] SOLUTION: Introduce product naturally
[15-25s] DEMO: Show product in action
[25-28s] RESULTS: Transformation/social proof
[28-30s] CTA: "Link in bio" / "Shop now"

### Testimonial Style:
[0-2s] HOOK: "This [product] changed my life"
[2-10s] BEFORE: Life before product
[10-20s] DISCOVERY: How I found it
[20-27s] AFTER: Results/transformation
[27-30s] CTA: Recommendation + link

### Tutorial/How-to:
[0-2s] HOOK: "How to [achieve result] in [time]"
[2-25s] STEPS: Step-by-step with product
[25-28s] RESULT: Final outcome
[28-30s] CTA: Get yours

## OUTPUT FORMAT (JSON)
```json
{
  "script": {
    "concept": "Mô tả ngắn concept video",
    "style": "UGC/Professional/Tutorial",
    "duration": 30,
    "scenes": [
      {
        "timestamp": "0-2s",
        "scene_type": "hook",
        "dialogue": "Text/voiceover",
        "action": "Mô tả hành động",
        "text_overlay": "Text trên màn hình",
        "product_placement": "Cách show sản phẩm"
      }
    ],
    "music_recommendation": "Loại nhạc/trending sound",
    "creator_brief": "Hướng dẫn cho creator/actor",
    "a_b_test_variations": [
      "Hook variation 1",
      "Hook variation 2"
    ]
  }
}
```

## VÍ DỤ (Skincare Product - 30s)

**Concept:** UGC style - Girl khoe da sau khi dùng sản phẩm

**Script:**
```
[0-2s] HOOK
Dialogue: "I was today years old when I found out WHY my skincare wasn't working"
Action: Close-up mặt, expression shocked
Text: "WAIT WHAT 😱"

[2-7s] PROBLEM
Dialogue: "Tôi đã dùng đủ loại serum vitamin C mà da vẫn xỉn, vẫn thâm"
Action: Cầm 3-4 chai serum khác nhau, lắc đầu
Text: "❌ Nothing worked"

[7-12s] DISCOVERY
Dialogue: "Cho đến khi dermatologist nói: Vitamin C bạn dùng đã bị OXY HÓA"
Action: Show chai vitamin C bị đổi màu vàng/nâu
Text: "oxidized = useless"

[12-20s] SOLUTION
Dialogue: "{Product} khác biệt vì công nghệ {technology} giữ vitamin C ổn định 100%"
Action: Show sản phẩm, zoom vào texture, apply lên da
Text: "✓ Stable formula"

[20-27s] RESULTS
Dialogue: "2 tuần sau - da sáng lên 2 tone, thâm mờ hẳn"
Action: Before/after comparison, glow under natural light
Text: "2 WEEKS ✨"

[27-30s] CTA
Dialogue: "Link trong bio - đang sale 30%"
Action: Point up + show product again
Text: "🔗 LINK IN BIO - 30% OFF"
```
"""
```

---

## 🏠 3. LANDING PAGE COPY PROMPTS

### 3.1 Sales Landing Page

```python
LANDING_PAGE_PROMPT = """
## NHIỆM VỤ
Viết copy hoàn chỉnh cho Landing Page bán hàng.

## THÔNG TIN SẢN PHẨM
- Tên sản phẩm: {product_name}
- Giá: {price}
- Offer: {offer}
- USP: {usp}
- Features: {features}
- Benefits: {benefits}
- Target audience: {target_audience}
- Pain points: {pain_points}

## CẤU TRÚC LANDING PAGE

### Section 1: HERO
- Headline (USP chính, 6-12 từ)
- Subheadline (Mở rộng headline, 15-25 từ)
- CTA Button text
- Hero image direction

### Section 2: PROBLEM
- Headline section
- 3-4 pain points (với emotional triggers)
- Transition to solution

### Section 3: SOLUTION
- Introduce product as THE solution
- How it works (3 steps)
- Key differentiators

### Section 4: FEATURES & BENEFITS
- 4-6 features
- Mỗi feature có: Icon idea, Feature name, Benefit description

### Section 5: SOCIAL PROOF
- 3 testimonials (với format: quote, name, title, result)
- Trust badges suggestions
- Stats/Numbers

### Section 6: PRICING/OFFER
- Price presentation
- What's included
- Bonuses (nếu có)
- Guarantee

### Section 7: FAQ
- 5-7 câu hỏi thường gặp
- Objection handling

### Section 8: FINAL CTA
- Urgency/Scarcity element
- Risk reversal
- CTA button

## OUTPUT FORMAT (JSON)
```json
{
  "landing_page": {
    "hero": {
      "headline": "...",
      "subheadline": "...",
      "cta_button": "...",
      "image_direction": "..."
    },
    "problem": {
      "section_headline": "...",
      "pain_points": [
        {"emoji": "😫", "text": "..."},
        {"emoji": "😤", "text": "..."}
      ],
      "transition": "..."
    },
    "solution": {
      "intro": "...",
      "how_it_works": [
        {"step": 1, "title": "...", "description": "..."},
        {"step": 2, "title": "...", "description": "..."},
        {"step": 3, "title": "...", "description": "..."}
      ],
      "differentiators": ["...", "...", "..."]
    },
    "features": [
      {
        "icon": "⚡",
        "name": "Feature name",
        "benefit": "What this means for customer"
      }
    ],
    "social_proof": {
      "testimonials": [
        {
          "quote": "...",
          "name": "Nguyễn Văn A",
          "title": "CEO, Company X",
          "result": "Kết quả cụ thể",
          "avatar_suggestion": "..."
        }
      ],
      "trust_badges": ["...", "..."],
      "stats": [
        {"number": "10,000+", "label": "Khách hàng"},
        {"number": "98%", "label": "Hài lòng"}
      ]
    },
    "pricing": {
      "original_price": "2,000,000đ",
      "sale_price": "1,400,000đ",
      "discount": "30%",
      "includes": ["Item 1", "Item 2"],
      "bonuses": [
        {"name": "Bonus 1", "value": "500,000đ"}
      ],
      "guarantee": "Hoàn tiền 100% trong 30 ngày nếu không hài lòng"
    },
    "faq": [
      {"question": "...", "answer": "..."}
    ],
    "final_cta": {
      "headline": "...",
      "urgency": "Chỉ còn X suất với giá này",
      "cta_button": "...",
      "subtext": "..."
    }
  }
}
```
"""
```

### 3.2 Lead Generation Landing Page

```python
LEAD_GEN_LP_PROMPT = """
## NHIỆM VỤ
Viết copy cho Lead Generation Landing Page (thu thập email/phone).

## THÔNG TIN
- Lead magnet: {lead_magnet} (ebook, webinar, free trial, consultation...)
- Value proposition: {value_prop}
- Target audience: {target_audience}

## CẤU TRÚC LEAD GEN PAGE

### Above the Fold:
- Headline: Value của lead magnet
- Subheadline: Vì sao họ cần
- Form fields cần thiết
- CTA button
- Trust indicator ngay dưới form

### Below the Fold:
- What you'll learn/get (bullet points)
- About author/company (nếu relevant)
- Mini testimonials
- FAQ (2-3 câu)

## OUTPUT FORMAT (JSON)
```json
{
  "lead_gen_page": {
    "headline": "...",
    "subheadline": "...",
    "form": {
      "fields": ["Họ tên", "Email", "Số điện thoại"],
      "cta_button": "Nhận ngay miễn phí",
      "privacy_text": "Chúng tôi tôn trọng quyền riêng tư của bạn"
    },
    "bullet_points": {
      "headline": "Bạn sẽ nhận được:",
      "points": [
        "✓ Point 1 với benefit",
        "✓ Point 2 với benefit"
      ]
    },
    "trust_indicators": ["Đã có 5,000+ người tải", "Miễn phí 100%"],
    "mini_testimonial": {
      "quote": "...",
      "name": "..."
    }
  }
}
```
"""
```

---

## 🎬 4. VIDEO SCRIPT PROMPTS

### 4.1 YouTube Video Script

```python
YOUTUBE_SCRIPT_PROMPT = """
## NHIỆM VỤ
Viết script video YouTube {duration} phút.

## THÔNG TIN VIDEO
- Chủ đề: {topic}
- Loại video: {video_type}
  • educational: Hướng dẫn, tutorial
  • entertainment: Giải trí
  • review: Đánh giá sản phẩm
  • vlog: Vlog cá nhân
  • comparison: So sánh

- Target audience: {audience}
- Keywords mục tiêu: {keywords}

## CẤU TRÚC YOUTUBE VIDEO

### 1. HOOK (0-30 giây) - QUAN TRỌNG NHẤT
- Pattern interrupt
- Promise value
- Create curiosity
- Optional: Teaser kết quả

### 2. INTRO (30s-1m)
- Channel intro (ngắn)
- Video overview
- Why they should watch till the end

### 3. CONTENT (Main body)
- Chia thành chapters/sections rõ ràng
- Mỗi section: Point → Explanation → Example
- Transition giữa các sections
- B-roll suggestions

### 4. CTA MID-VIDEO
- Subscribe reminder
- Like reminder
- Comment engagement

### 5. CONCLUSION
- Recap key points
- Final takeaway
- Strong CTA

### 6. END SCREEN
- Recommend related video
- Subscribe again

## OUTPUT FORMAT (JSON)
```json
{
  "video_script": {
    "title_options": [
      "Title 1 (with keyword)",
      "Title 2 (curiosity)",
      "Title 3 (number)"
    ],
    "thumbnail_concepts": [
      "Concept 1: ...",
      "Concept 2: ..."
    ],
    "description": "YouTube description with keywords...",
    "tags": ["tag1", "tag2"],
    "chapters": [
      {"timestamp": "0:00", "title": "Intro"},
      {"timestamp": "0:30", "title": "Chapter 1"}
    ],
    "script": {
      "hook": {
        "duration": "0-30s",
        "dialogue": "...",
        "visual": "...",
        "text_overlay": "..."
      },
      "sections": [
        {
          "title": "Section 1",
          "duration": "1:00-3:00",
          "key_points": ["Point 1", "Point 2"],
          "dialogue": "Full script...",
          "b_roll": ["Suggestion 1", "Suggestion 2"],
          "graphics": ["Graphic idea 1"]
        }
      ],
      "cta_mid": {
        "timestamp": "~50% video",
        "dialogue": "..."
      },
      "conclusion": {
        "recap": ["Point 1", "Point 2"],
        "final_thought": "...",
        "cta": "..."
      }
    }
  }
}
```
"""
```

### 4.2 Video Ads Script (Professional)

```python
VIDEO_ADS_SCRIPT_PROMPT = """
## NHIỆM VỤ
Viết script video quảng cáo {duration} giây cho {platform}.

## THÔNG TIN
- Sản phẩm: {product}
- Mục tiêu: {objective}
- Budget production: {budget_level} (low/medium/high)
- Style: {style} (testimonial/demo/story/animated)

## SCRIPT FORMATS BY DURATION

### 6 giây (YouTube Bumper):
- 1 message duy nhất
- Brand recall focus
[0-4s] Key message/visual
[4-6s] Logo + CTA

### 15 giây:
[0-3s] HOOK - Problem/Attention
[3-10s] SOLUTION - Product demo/benefit
[10-15s] CTA + BRANDING

### 30 giây:
[0-5s] HOOK - Emotional trigger
[5-15s] PROBLEM - Relate to audience
[15-25s] SOLUTION - Product as hero
[25-30s] CTA + OFFER

### 60 giây:
[0-5s] HOOK
[5-15s] PROBLEM/SITUATION
[15-35s] SOLUTION + DEMO
[35-50s] SOCIAL PROOF
[50-60s] CTA + BRANDING

## OUTPUT FORMAT (JSON)
```json
{
  "video_ad": {
    "concept": "...",
    "duration": 30,
    "production_notes": {
      "style": "...",
      "talent_needed": "...",
      "location": "...",
      "props": ["..."]
    },
    "script": [
      {
        "scene": 1,
        "timestamp": "0-5s",
        "type": "hook",
        "visual": "Mô tả cảnh quay",
        "audio": {
          "dialogue": "...",
          "voiceover": "...",
          "sfx": "...",
          "music": "..."
        },
        "text_overlay": "...",
        "transition": "Cut to..."
      }
    ],
    "end_card": {
      "logo_placement": "...",
      "cta_text": "...",
      "contact_info": "..."
    },
    "a_b_test_suggestions": [
      "Test different hooks",
      "Test with/without testimonial"
    ]
  }
}
```
"""
```

---

## 🛠️ UTILITY PROMPTS

### Brand Voice Analyzer

```python
BRAND_VOICE_ANALYZER = """
## NHIỆM VỤ
Phân tích brand voice từ content samples được cung cấp.

## CONTENT SAMPLES
{content_samples}

## PHÂN TÍCH VÀ OUTPUT

```json
{
  "brand_voice_analysis": {
    "tone": {
      "primary": "professional/friendly/playful/luxury",
      "secondary": "...",
      "confidence_score": 0.85
    },
    "language_style": {
      "formality": "formal/casual/mixed",
      "sentence_length": "short/medium/long",
      "vocabulary_level": "simple/intermediate/advanced"
    },
    "emotional_attributes": ["inspiring", "trustworthy", "exciting"],
    "writing_patterns": {
      "common_phrases": ["Phrase 1", "Phrase 2"],
      "avoided_words": ["Word 1", "Word 2"],
      "punctuation_style": "Heavy emoji/Minimal/Standard"
    },
    "recommendations": {
      "do": ["Nên làm 1", "Nên làm 2"],
      "dont": ["Tránh 1", "Tránh 2"]
    }
  }
}
```
"""
```

### Content Repurposing

```python
CONTENT_REPURPOSE_PROMPT = """
## NHIỆM VỤ
Repurpose nội dung gốc thành các format khác nhau.

## NỘI DUNG GỐC
{original_content}

## LOẠI NỘI DUNG GỐC
{content_type} (blog/video/podcast/webinar)

## REPURPOSE THÀNH
1. 5 Twitter/X posts
2. 3 LinkedIn posts
3. 1 Instagram carousel (10 slides)
4. 5 quote graphics text
5. 1 email newsletter
6. 3 TikTok/Reels hooks

## OUTPUT FORMAT
```json
{
  "repurposed_content": {
    "twitter_posts": [...],
    "linkedin_posts": [...],
    "instagram_carousel": {
      "slides": [...]
    },
    "quote_graphics": [...],
    "email_newsletter": {...},
    "short_video_hooks": [...]
  }
}
```
"""
```

---

## 📁 FILE STRUCTURE CHO PROMPTS

```
prompts/
├── base/
│   ├── system_prompt.py
│   └── brand_context.py
│
├── social/
│   ├── facebook.py
│   ├── instagram.py
│   ├── tiktok.py
│   ├── linkedin.py
│   └── twitter.py
│
├── ads/
│   ├── facebook_ads.py
│   ├── google_ads.py
│   ├── tiktok_ads.py
│   └── video_ads.py
│
├── landing/
│   ├── sales_page.py
│   ├── lead_gen.py
│   └── product_page.py
│
├── video/
│   ├── youtube.py
│   ├── short_form.py
│   └── ads_script.py
│
├── utility/
│   ├── analyzer.py
│   ├── repurpose.py
│   └── translate.py
│
└── examples/
    ├── fnb_examples.py
    ├── beauty_examples.py
    ├── education_examples.py
    └── ecommerce_examples.py
```

---

*Tiếp theo: Phần 3 - MVP Code*
