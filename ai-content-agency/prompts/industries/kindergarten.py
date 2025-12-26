"""
🎒 PROMPT TEMPLATES CHO NGÀNH MẦM NON / TRƯỜNG MẦM NON
Specialized prompts for Kindergarten & Preschool content

Đặc thù ngành:
- Target: Phụ huynh có con 1-6 tuổi
- Tone: Thân thiện, ấm áp, đáng tin cậy
- Content: Hoạt động hàng ngày, giáo dục, sự kiện
- Sensitive: Hình ảnh trẻ em, an toàn, giáo dục
"""

# ============================================================
# SYSTEM PROMPT - BASE CHO TẤT CẢ CONTENT MẦM NON
# ============================================================

KINDERGARTEN_SYSTEM_PROMPT = """
Bạn là Content Creator chuyên nghiệp với 10+ năm kinh nghiệm trong ngành GIÁO DỤC MẦM NON.
Bạn hiểu sâu sắc tâm lý phụ huynh và cách truyền thông hiệu quả cho các trường mầm non.

## BRAND CONTEXT
- Tên trường: {school_name}
- Slogan: {slogan}
- Phương pháp giáo dục: {teaching_method} (Montessori/Reggio Emilia/STEAM/Truyền thống/Kết hợp)
- Độ tuổi nhận: {age_range}
- Địa chỉ: {location}
- USP: {usp}

## TARGET AUDIENCE
Phụ huynh có con nhỏ 1-6 tuổi:
- Độ tuổi phụ huynh: 25-40
- Quan tâm: Sự phát triển toàn diện của con, an toàn, môi trường học tập
- Pain points: Lo lắng khi gửi con, muốn biết con học gì mỗi ngày
- Desires: Con vui vẻ, phát triển tốt, được quan tâm cá nhân

## TONE OF VOICE
- Thân thiện, ấm áp như người thân trong gia đình
- Chuyên nghiệp nhưng không cứng nhắc
- Tích cực, truyền cảm hứng
- Đáng tin cậy, minh bạch

## QUY TẮC BẮT BUỘC
1. KHÔNG đăng hình ảnh trẻ em mà không có consent (chỉ gợi ý, không mô tả cụ thể khuôn mặt)
2. Luôn nhấn mạnh yếu tố AN TOÀN và CHĂM SÓC
3. Sử dụng ngôn ngữ tích cực, tránh tiêu cực
4. Gọi học sinh là "các bé", "các con", "những thiên thần nhỏ"
5. Gọi phụ huynh là "Ba Mẹ", "Quý phụ huynh"
6. Emoji phù hợp: 🎒 📚 🌈 ⭐ 🎨 🎵 💕 🏫 👨‍👩‍👧‍👦
7. KHÔNG dùng từ ngữ tiêu cực về trẻ em
8. Hashtags: #{school_hashtag} #MamNon #GiaoDucMamNon #TruongMamNon
"""

# ============================================================
# CONTENT PILLARS CHO TRƯỜNG MẦM NON
# ============================================================

CONTENT_PILLARS = """
## 5 CONTENT PILLARS CHO TRƯỜNG MẦM NON

1. 📸 HOẠT ĐỘNG HÀNG NGÀY (40%)
   - Học tập trên lớp
   - Giờ ăn, giờ ngủ
   - Vui chơi ngoài trời
   - Góc học tập theo chủ đề
   
2. 🎉 SỰ KIỆN & LỄ HỘI (20%)
   - Sinh nhật các bé
   - Lễ hội (Trung thu, Halloween, Giáng sinh, Tết...)
   - Field trip / Dã ngoại
   - Ngày hội gia đình
   
3. 📚 KIẾN THỨC NUÔI DẠY CON (20%)
   - Tips cho phụ huynh
   - Phát triển kỹ năng theo độ tuổi
   - Dinh dưỡng cho trẻ
   - Tâm lý trẻ em
   
4. 🏫 GIỚI THIỆU TRƯỜNG (10%)
   - Cơ sở vật chất
   - Đội ngũ giáo viên
   - Phương pháp giảng dạy
   - Thành tích, chứng nhận
   
5. 💬 TESTIMONIALS & STORY (10%)
   - Feedback phụ huynh
   - Câu chuyện của các bé
   - Alumni stories
   - Behind the scenes
"""

# ============================================================
# SOCIAL MEDIA PROMPTS
# ============================================================

DAILY_ACTIVITY_POST = """
## NHIỆM VỤ
Tạo {num_posts} bài post Facebook về HOẠT ĐỘNG HÀNG NGÀY của trường.

## THÔNG TIN
- Hoạt động: {activity_type}
  (Học tập / Vui chơi / Ăn trưa / Giờ ngủ / Hoạt động ngoài trời / Góc sáng tạo)
- Chủ đề tuần/tháng: {weekly_theme}
- Lớp: {class_name}
- Nội dung cụ thể: {activity_details}

## YÊU CẦU
1. Hook: Mở đầu thân thiện, gợi cảm xúc
2. Body: Mô tả hoạt động, highlight điểm đặc biệt
3. Educational value: Bé học được gì từ hoạt động này
4. CTA: Mời phụ huynh tương tác

## VÍ DỤ THAM KHẢO

### Hoạt động học tập:
"📚 Hôm nay các bé lớp Mầm cùng khám phá thế giới đại dương! 🐠

Qua bài học "Sinh vật biển", các con được:
✨ Tìm hiểu về các loài cá, san hô
✨ Sáng tạo tranh cá từ giấy màu
✨ Chơi trò chơi "Đi câu cá" rèn kỹ năng vận động tinh

Cô thấy các bé rất hào hứng khi được tự tay làm chú cá của riêng mình! 

💬 Ba Mẹ thử hỏi con về "Con cá yêu thích của con" tối nay nhé!

#TruongMamNon{school_name} #HocMaChoi #SinhVatBien"

### Giờ ăn:
"🍚 Thực đơn hôm nay của các thiên thần nhỏ:

🥗 Cơm gạo lứt
🍗 Gà hấp nấm
🥦 Canh bí đỏ thịt bằm
🍊 Tráng miệng: Cam tươi

Các bé ăn ngon miệng lắm ạ! Nhiều bé còn xin thêm cơm nữa 😋

📌 Menu được chuyên gia dinh dưỡng thiết kế, đảm bảo đủ 4 nhóm chất cho sự phát triển của con!

#MamNon #DinhDuongChoTre #AnNgonMienManh"

## OUTPUT FORMAT (JSON)
```json
{{
  "posts": [
    {{
      "hook": "Mở đầu thu hút",
      "body": "Nội dung chính",
      "educational_value": "Giá trị giáo dục",
      "cta": "Kêu gọi tương tác",
      "hashtags": ["#tag1", "#tag2"],
      "image_suggestion": "Gợi ý hình ảnh (không mô tả mặt trẻ)",
      "best_time": "Thời gian đăng tốt nhất"
    }}
  ]
}}
```
"""

EVENT_ANNOUNCEMENT_POST = """
## NHIỆM VỤ
Tạo bài post THÔNG BÁO SỰ KIỆN cho trường mầm non.

## THÔNG TIN SỰ KIỆN
- Tên sự kiện: {event_name}
- Loại sự kiện: {event_type}
  (Lễ hội / Field trip / Ngày hội / Sinh nhật tháng / Biểu diễn / Họp phụ huynh)
- Thời gian: {event_date}
- Địa điểm: {location}
- Đối tượng: {participants}
- Chi tiết: {event_details}
- Yêu cầu phụ huynh: {parent_requirements}

## CẤU TRÚC BÀI POST

### Announcement (Trước sự kiện):
1. Hook hấp dẫn về sự kiện
2. Thông tin chi tiết (5W1H)
3. Những điều thú vị đang chờ đón
4. Checklist cho phụ huynh
5. CTA đăng ký/xác nhận

### Recap (Sau sự kiện):
1. Hook - highlight moment
2. Tóm tắt sự kiện
3. Những khoảnh khắc đáng nhớ
4. Cảm ơn
5. Teaser sự kiện tiếp theo

## VÍ DỤ

### Trước sự kiện Trung Thu:
"🏮 THÔNG BÁO: TẾT TRUNG THU YÊU THƯƠNG 2024 🌕

Trường Mầm Non {school_name} trân trọng kính mời Quý Phụ Huynh và các bé tham dự:

🎊 TẾT TRUNG THU YÊU THƯƠNG
📅 Thứ Bảy, 14/09/2024
⏰ 17:00 - 20:00
📍 Sân trường {school_name}

✨ CHƯƠNG TRÌNH:
• Rước đèn cùng chị Hằng, chú Cuội
• Múa lân sôi động
• Phá cỗ đêm trăng
• Văn nghệ "Bé yêu trăng"
• Quà Trung Thu cho tất cả các bé

📝 PHỤ HUYNH LƯU Ý:
☑️ Xác nhận tham dự trước 10/09
☑️ Các bé mặc đồ truyền thống nếu có
☑️ Mỗi gia đình mang 1 chiếc đèn lồng

💕 Hãy cùng con tạo nên những kỷ niệm tuổi thơ đáng nhớ!

👉 Đăng ký: [Link/Comment/Inbox]

#TetTrungThu2024 #{school_hashtag} #MamNon"

## OUTPUT FORMAT (JSON)
```json
{{
  "announcement_post": {{
    "hook": "...",
    "event_info": "...",
    "highlights": ["...", "..."],
    "checklist": ["...", "..."],
    "cta": "...",
    "hashtags": ["..."],
    "image_suggestion": "..."
  }},
  "reminder_post": {{
    "content": "Bài nhắc nhở 1-2 ngày trước"
  }},
  "recap_post": {{
    "content": "Bài tổng kết sau sự kiện"
  }}
}}
```
"""

PARENTING_TIPS_POST = """
## NHIỆM VỤ
Tạo bài post CHIA SẺ KIẾN THỨC NUÔI DẠY CON.

## THÔNG TIN
- Chủ đề: {topic}
- Độ tuổi áp dụng: {age_group}
- Mức độ chi tiết: {detail_level} (quick_tip / detailed_guide / series)

## DANH MỤC CHỦ ĐỀ PHỔ BIẾN

1. **Phát triển ngôn ngữ**
   - Cách đọc sách cho con
   - Trò chuyện với con hàng ngày
   - Dạy con song ngữ
   
2. **Phát triển vận động**
   - Hoạt động trong nhà
   - Hoạt động ngoài trời
   - Vận động tinh (cầm bút, cắt giấy...)
   
3. **Phát triển cảm xúc - xã hội**
   - Dạy con quản lý cảm xúc
   - Kỹ năng giao tiếp
   - Giải quyết xung đột
   
4. **Dinh dưỡng**
   - Thực đơn theo độ tuổi
   - Xử lý biếng ăn
   - Snack healthy
   
5. **Giấc ngủ**
   - Routine trước khi ngủ
   - Xử lý khó ngủ
   - Giấc ngủ trưa
   
6. **Chuẩn bị vào lớp 1**
   - Kỹ năng cần có
   - Tâm lý sẵn sàng
   - Hoạt động chuẩn bị

## VÍ DỤ

### Quick Tip:
"💡 TIPS: 5 câu hỏi thay vì 'Hôm nay con học gì?'

Câu hỏi 'Con học gì?' thường nhận được 'Không có gì' 😅

Thử những câu này nhé:
1️⃣ 'Điều gì khiến con cười hôm nay?'
2️⃣ 'Con chơi với bạn nào? Chơi trò gì?'
3️⃣ 'Cô giáo có kể chuyện gì vui không?'
4️⃣ 'Con giúp đỡ ai hôm nay?'
5️⃣ 'Mai con muốn mang gì đến lớp?'

Hỏi cụ thể = Câu chuyện cụ thể! 🌟

💬 Ba Mẹ có tip nào hay không, chia sẻ bên dưới nhé!

#TipsChaMe #GiaoDucSom #MamNon"

### Detailed Guide:
"📚 HƯỚNG DẪN: Dạy con QUẢN LÝ CẢM XÚC (3-6 tuổi)

Các bé tuổi mầm non đang học cách hiểu và kiểm soát cảm xúc. Đây là giai đoạn quan trọng!

🧠 VÌ SAO CON HAY 'ĂN VẠ'?
Não bộ phần điều khiển cảm xúc (prefrontal cortex) chưa phát triển hoàn chỉnh đến năm 25 tuổi! Con không hư - con đang HỌC.

✅ 4 BƯỚC GIÚP CON:

**Bước 1: NHẬN DIỆN cảm xúc**
• 'Con đang buồn/giận/sợ phải không?'
• Đọc sách về cảm xúc (Color Monster, In My Heart...)
• Làm 'bảng cảm xúc' cùng con

**Bước 2: CHẤP NHẬN cảm xúc**
• 'Không sao, ai cũng có lúc buồn'
• Ôm con, ở bên con
• KHÔNG nói 'Có gì đâu mà khóc'

**Bước 3: DẠY CÁCH XỬ LÝ**
• Hít thở sâu (thổi nến tưởng tượng)
• Góc bình yên (nơi con có thể ngồi lại)
• Nặn đất sét, vẽ tranh

**Bước 4: KHEN NGỢI tiến bộ**
• 'Con giỏi quá, đã bình tĩnh lại rồi!'
• Ghi nhận mọi cố gắng nhỏ

💕 Kiên nhẫn nhé Ba Mẹ! Đây là hành trình dài nhưng xứng đáng.

📌 SAVE lại để áp dụng mỗi ngày!

#QuanLyCamXuc #DayConKyNangSong #MamNon"

## OUTPUT FORMAT (JSON)
```json
{{
  "posts": [
    {{
      "type": "quick_tip | detailed_guide | carousel",
      "hook": "...",
      "main_content": "...",
      "actionable_steps": ["...", "..."],
      "cta": "...",
      "hashtags": ["..."],
      "save_worthy": true,
      "carousel_slides": ["Slide 1", "Slide 2"] // nếu là carousel
    }}
  ]
}}
```
"""

ENROLLMENT_CAMPAIGN_POST = """
## NHIỆM VỤ
Tạo content cho CHIẾN DỊCH TUYỂN SINH trường mầm non.

## THÔNG TIN
- Năm học: {school_year}
- Độ tuổi tuyển: {age_range}
- Ưu đãi: {promotion}
- Deadline: {deadline}
- USP của trường: {school_usp}

## CONTENT FUNNEL

### 1. AWARENESS (Nhận biết)
- Giới thiệu trường
- Phương pháp giáo dục
- Cơ sở vật chất

### 2. CONSIDERATION (Cân nhắc)
- So sánh ưu điểm
- Testimonials phụ huynh
- Thành tích học sinh

### 3. DECISION (Quyết định)
- Ưu đãi tuyển sinh
- Open day
- Đăng ký tư vấn

## VÍ DỤ

### Awareness Post:
"🌟 Tại sao 500+ gia đình tin chọn {school_name}?

✅ Phương pháp Montessori chuẩn quốc tế
✅ Tỷ lệ 1 cô : 8 bé - quan tâm từng con
✅ 100% giáo viên có chứng chỉ quốc tế
✅ Bếp ăn đạt chuẩn VSATTP 5 sao
✅ Camera 24/7 - Ba Mẹ yên tâm

'Nơi con được là chính mình' 💕

👉 Tìm hiểu thêm: [Link website]

#TuyenSinh2024 #{school_hashtag}"

### Testimonial Post:
"💬 'Điều tôi ấn tượng nhất là cách các cô lắng nghe con...'

Chị Minh Anh - Mẹ bé Bông (4 tuổi):

'Bông nhút nhát, hay khóc khi mới đi học. Nhưng chỉ sau 2 tuần ở {school_name}, con đã háo hức đến trường mỗi sáng.

Các cô không ép con, mà kiên nhẫn chờ con sẵn sàng. Con được tự chọn hoạt động, tự khám phá. Giờ Bông tự tin, hay kể chuyện và yêu việc học lắm!'

📍 Đăng ký tham quan trường: [Link]

#FeedbackPhuHuynh #MamNon{school_name}"

### Promotion Post:
"🎁 ƯU ĐÃI TUYỂN SINH 2024-2025

🔥 ĐĂNG KÝ TRƯỚC 30/06:
✨ Giảm 30% học phí tháng đầu
✨ Miễn phí bộ đồng phục
✨ Tặng cặp sách + bình nước
✨ Ưu tiên chọn lớp

📅 OPEN DAY: 15-16/06/2024
⏰ 8:30 - 11:30 & 14:00 - 17:00
📍 {school_address}

Tại Open Day:
• Tham quan lớp học
• Gặp gỡ giáo viên
• Con được trải nghiệm 1 buổi học
• Tư vấn 1:1 với Ban Giám Hiệu

👉 ĐĂNG KÝ NGAY: [Link/Hotline]
📞 Hotline: 0xxx xxx xxx

#TuyenSinh2024 #OpenDay #MamNon"

## OUTPUT FORMAT (JSON)
```json
{{
  "campaign_posts": {{
    "awareness": [{{...}}],
    "consideration": [{{...}}],
    "decision": [{{...}}]
  }},
  "ad_copies": {{
    "headlines": ["...", "..."],
    "primary_texts": ["...", "..."],
    "cta_buttons": ["Đăng ký ngay", "Tìm hiểu thêm"]
  }},
  "landing_page_sections": {{
    "hero": "...",
    "benefits": ["...", "..."],
    "testimonials": ["...", "..."],
    "faq": [{{...}}]
  }}
}}
```
"""

# ============================================================
# VIDEO SCRIPT FOR KINDERGARTEN
# ============================================================

KINDERGARTEN_VIDEO_SCRIPT = """
## NHIỆM VỤ
Viết script video {duration} giây cho trường mầm non.

## LOẠI VIDEO
- {video_type}:
  • tour: Tour trường (cơ sở vật chất)
  • daily_life: Một ngày của bé
  • teacher_intro: Giới thiệu cô giáo
  • testimonial: Phụ huynh chia sẻ
  • activity: Highlight hoạt động
  • educational: Tips cho phụ huynh

## VÍ DỤ SCRIPT

### Video Tour Trường (60s):
```
[0-5s] HOOK
Visual: Cổng trường với banner chào đón
Text: "Bên trong ngôi trường hạnh phúc 💕"
Audio: Tiếng cười trẻ em + nhạc vui

[5-15s] LỚP HỌC
Visual: Các góc học tập Montessori
Voiceover: "Lớp học được thiết kế theo chuẩn Montessori - mọi thứ vừa tầm tay bé, để con tự do khám phá"
Text: "Chuẩn Montessori Quốc tế"

[15-25s] SÂN CHƠI
Visual: Sân chơi ngoài trời với cầu trượt, nhà bóng
Voiceover: "Sân chơi an toàn với mặt đất cao su, nơi các bé thỏa sức vận động mỗi ngày"
Text: "Sân chơi an toàn 500m²"

[25-35s] BẾP & PHÒNG ĂN
Visual: Bếp sạch sẽ, các bé ngồi ăn
Voiceover: "Bếp đạt chuẩn 5 sao, menu được chuyên gia dinh dưỡng thiết kế theo tuần"
Text: "Bếp chuẩn 5 sao"

[35-45s] ĐỘI NGŨ
Visual: Các cô giáo tươi cười
Voiceover: "100% giáo viên có chứng chỉ quốc tế, với tình yêu và sự kiên nhẫn dành cho từng bé"
Text: "100% GV chứng chỉ quốc tế"

[45-55s] HOẠT ĐỘNG
Visual: Montage các hoạt động vui
Voiceover: "Mỗi ngày là một hành trình khám phá đầy niềm vui tại {school_name}"

[55-60s] CTA
Visual: Logo + thông tin liên hệ
Text: "Đăng ký tham quan: 0xxx xxx xxx"
Voiceover: "Đăng ký tham quan miễn phí ngay hôm nay!"
```

### Video "Một ngày của bé" (45s):
```
[0-3s] HOOK
Text: "7:30 AM - Một ngày ở {school_name}"
Visual: Mặt trời mọc, cổng trường

[3-10s] ĐÓN TRẺ
Visual: Bé vẫy tay mẹ, đi vào lớp
Voiceover: "Mỗi sáng, các bé được cô đón với nụ cười ấm áp"

[10-18s] HỌC TẬP
Visual: Hoạt động góc, học nhóm
Voiceover: "Học qua chơi - con được tự do chọn hoạt động yêu thích"

[18-25s] GIỜ ĂN
Visual: Các bé ăn ngon miệng
Voiceover: "Bữa trưa đủ chất với thực phẩm tươi mỗi ngày"

[25-32s] NGỦ TRƯA
Visual: Phòng ngủ yên tĩnh
Voiceover: "Giấc ngủ ngon để con có năng lượng cho buổi chiều"

[32-40s] CHIỀU
Visual: Hoạt động ngoài trời, văn nghệ
Voiceover: "Buổi chiều với thể dục, âm nhạc và nghệ thuật"

[40-45s] CTA
Visual: Bé vẫy tay bye, logo
Text: "Trải nghiệm 1 ngày cùng con: 0xxx"
```

## OUTPUT FORMAT (JSON)
```json
{{
  "script": {{
    "concept": "...",
    "total_duration": 60,
    "segments": [
      {{
        "timestamp": "0-5s",
        "visual": "...",
        "voiceover": "...",
        "text_overlay": "...",
        "audio_note": "..."
      }}
    ],
    "music_suggestion": "...",
    "thumbnail": "..."
  }}
}}
```
"""

# ============================================================
# CONTENT CALENDAR TEMPLATE
# ============================================================

MONTHLY_CONTENT_CALENDAR = """
## CONTENT CALENDAR MẪU - THÁNG {month}

### TUẦN 1: {week1_theme}
| Ngày | Loại content | Nội dung | Platform |
|------|-------------|----------|----------|
| T2 | Daily Activity | Hoạt động đầu tuần | FB, IG |
| T3 | Tips | Tip nuôi dạy con | FB, IG |
| T4 | Daily Activity | Highlight lớp | FB |
| T5 | Behind the scenes | Chuẩn bị bữa ăn | IG Story |
| T6 | Weekly recap | Tổng kết tuần | FB, IG |
| T7 | Fun fact | Fact thú vị về trẻ | IG |
| CN | Nghỉ hoặc Evergreen | - | - |

### TUẦN 2: {week2_theme}
...

### SỰ KIỆN THÁNG {month}:
{monthly_events}

### HASHTAG THÁNG:
#{school_hashtag} #{monthly_hashtag}
"""

# ============================================================
# CRISIS COMMUNICATION
# ============================================================

CRISIS_TEMPLATES = """
## TEMPLATE THÔNG BÁO KHẨN CẤP

### 1. Thông báo nghỉ học (thời tiết/dịch bệnh):
"📢 THÔNG BÁO KHẨN

Trường Mầm Non {school_name} xin thông báo:

Do {reason}, trường sẽ tạm nghỉ học vào ngày {date}.

📌 Các lớp sẽ hoạt động trở lại bình thường từ ngày {return_date}.

Trong thời gian nghỉ, Quý Phụ Huynh có thể liên hệ hotline {hotline} nếu cần hỗ trợ.

Trường xin lỗi vì sự bất tiện này.

Trân trọng,
Ban Giám Hiệu"

### 2. Thông báo về sức khỏe:
"📢 THÔNG BÁO VỀ SỨC KHỎE

Kính gửi Quý Phụ Huynh,

Trường xin thông báo: {health_issue}

✅ CÁC BIỆN PHÁP TRƯỜNG ĐÃ THỰC HIỆN:
• {measure_1}
• {measure_2}
• {measure_3}

📌 PHỤ HUYNH LƯU Ý:
• {parent_note_1}
• {parent_note_2}

Trường cam kết đặt sức khỏe các con lên hàng đầu.

Mọi thắc mắc xin liên hệ: {contact}

Trân trọng,
Ban Giám Hiệu"
"""

# ============================================================
# FACEBOOK ADS TEMPLATES
# ============================================================

KINDERGARTEN_ADS_PROMPTS = """
## FACEBOOK ADS CHO TUYỂN SINH MẦM NON

### TARGETING GỢI Ý:
- Parents với con 1-6 tuổi
- Vị trí: Bán kính 5-10km quanh trường
- Interest: Parenting, Early childhood education, Montessori
- Behavior: Engaged parents

### AD FORMATS:

#### 1. Carousel Ad (Tour ảo):
Slide 1: Cổng trường - "Chào mừng đến {school_name}"
Slide 2: Lớp học - "Không gian học tập sáng tạo"
Slide 3: Sân chơi - "Nơi con thỏa sức vận động"
Slide 4: Bếp ăn - "Dinh dưỡng cho sự phát triển"
Slide 5: CTA - "Đăng ký tham quan ngay"

#### 2. Video Ad (15-30s):
Hook: "Làm thế nào để chọn trường mầm non phù hợp?"
Problem: Nỗi lo của ba mẹ
Solution: Giới thiệu trường
Social proof: "500+ gia đình đã tin chọn"
CTA: "Đăng ký tư vấn miễn phí"

#### 3. Lead Ad:
Primary text: "🎒 TUYỂN SINH 2024-2025
[Benefit 1]
[Benefit 2]
[Benefit 3]
🎁 Ưu đãi: {promotion}"
Headline: "Đăng ký tư vấn MIỄN PHÍ"
Form fields: Tên PH, SĐT, Tên bé, Tuổi bé

### AD COPY VARIATIONS:

#### Problem-focused:
"Bạn lo lắng khi gửi con đi học?
✓ Con có được quan tâm không?
✓ Con có ăn ngủ đủ không?
✓ Con có vui không?

Tại {school_name}, với tỷ lệ 1 cô : 8 bé, con bạn sẽ được chăm sóc như ở nhà 💕"

#### Benefit-focused:
"Tại {school_name}, con bạn sẽ:
✨ Học qua chơi theo phương pháp Montessori
✨ Phát triển ngôn ngữ với chương trình song ngữ
✨ Tự tin giao tiếp từ nhỏ
✨ Sẵn sàng tâm lý cho lớp 1"

#### Social proof:
"'Sau 1 tháng ở {school_name}, con tôi thay đổi hoàn toàn...'
- Chị Lan, mẹ bé An

Hơn 500 gia đình đã tin chọn. Bạn tiếp theo chứ?"
"""

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_seasonal_themes(month: int) -> dict:
    """Return seasonal themes and events for content planning"""
    themes = {
        1: {
            "theme": "Năm mới - Khởi đầu mới",
            "events": ["Tết Dương lịch", "Chuẩn bị Tết Nguyên đán"],
            "content_ideas": ["Mục tiêu năm mới cho bé", "DIY đồ trang trí Tết"]
        },
        2: {
            "theme": "Tết Nguyên đán",
            "events": ["Tết Nguyên đán", "Valentine"],
            "content_ideas": ["Các bé gói bánh chưng", "Trang phục truyền thống", "Lì xì đầu năm"]
        },
        3: {
            "theme": "Mùa xuân - Khám phá thiên nhiên",
            "events": ["8/3 - Ngày Quốc tế Phụ nữ"],
            "content_ideas": ["Quà 8/3 handmade", "Hoạt động ngoài trời", "Trồng cây xanh"]
        },
        4: {
            "theme": "Giỗ Tổ Hùng Vương",
            "events": ["Giỗ Tổ Hùng Vương", "30/4-1/5"],
            "content_ideas": ["Lịch sử Việt Nam cho bé", "Văn hóa truyền thống"]
        },
        5: {
            "theme": "Gia đình",
            "events": ["Ngày của Mẹ", "1/6"],
            "content_ideas": ["Quà cho mẹ", "Hoạt động gia đình cuối tuần"]
        },
        6: {
            "theme": "Mùa hè vui - Tết thiếu nhi",
            "events": ["1/6 - Tết Thiếu nhi", "Tổng kết năm học"],
            "content_ideas": ["Chương trình 1/6", "Lễ tổng kết", "Summer camp"]
        },
        7: {
            "theme": "Hè sôi động",
            "events": ["Summer camp", "Tuyển sinh"],
            "content_ideas": ["Hoạt động hè", "Đọc sách hè", "Tuyển sinh năm mới"]
        },
        8: {
            "theme": "Chuẩn bị năm học mới",
            "events": ["Tuyển sinh", "Open day"],
            "content_ideas": ["Tips chuẩn bị đi học", "Khai giảng sớm"]
        },
        9: {
            "theme": "Khai giảng - Trung thu",
            "events": ["Khai giảng", "Tết Trung thu"],
            "content_ideas": ["Ngày đầu đến lớp", "Lễ hội Trung thu", "Làm đèn lồng"]
        },
        10: {
            "theme": "Phụ nữ Việt Nam - Halloween",
            "events": ["20/10", "Halloween"],
            "content_ideas": ["Quà 20/10", "Halloween party", "Hóa trang"]
        },
        11: {
            "theme": "Ngày Nhà giáo",
            "events": ["20/11 - Ngày Nhà giáo Việt Nam"],
            "content_ideas": ["Tri ân cô giáo", "Quà handmade", "Văn nghệ 20/11"]
        },
        12: {
            "theme": "Giáng sinh - Năm mới",
            "events": ["Giáng sinh", "Tổng kết HK1", "New Year"],
            "content_ideas": ["Christmas party", "Ông già Noel", "Tổng kết học kỳ"]
        }
    }
    return themes.get(month, themes[1])


def get_age_appropriate_activities(age: int) -> list:
    """Return age-appropriate activities for content"""
    activities = {
        1: ["Giác quan", "Vận động thô", "Âm nhạc", "Chơi với đồ vật"],
        2: ["Vẽ nguệch ngoạc", "Xếp hình đơn giản", "Chơi cát nước", "Đọc sách tranh"],
        3: ["Cắt dán", "Vẽ tô màu", "Chơi đóng vai", "Xây dựng", "Kể chuyện"],
        4: ["Viết chữ", "Toán đơn giản", "STEM đơn giản", "Thể dục nhịp điệu", "Múa hát"],
        5: ["Chuẩn bị tiền tiểu học", "Đọc viết", "Toán tư duy", "Thí nghiệm khoa học", "Nghệ thuật"],
        6: ["Ôn luyện vào lớp 1", "Kỹ năng tự lập", "Làm việc nhóm", "Thuyết trình"]
    }
    return activities.get(age, activities[3])
