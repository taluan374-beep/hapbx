# 🚀 AI Content Agency

> Nền tảng tự động tạo content marketing với AI cho thị trường Việt Nam

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-green.svg)](https://python.org)
[![Next.js](https://img.shields.io/badge/Next.js-14-black.svg)](https://nextjs.org)

## 📖 Tổng quan

AI Content Agency là giải pháp SaaS giúp doanh nghiệp Việt Nam tự động hóa việc tạo content marketing, bao gồm:

- 📱 **Social Media Content** - Facebook, Instagram, TikTok, LinkedIn
- 🎯 **Ads Copy** - Facebook Ads, Google Ads, TikTok Ads
- 🏠 **Landing Page Copy** - Sales pages, Lead gen pages
- 🎬 **Video Scripts** - TikTok, Reels, YouTube
- 🖼️ **AI Images** - Product shots, Social graphics

## 🎯 Vấn đề giải quyết

| Cách truyền thống | AI Content Agency |
|-------------------|-------------------|
| Thuê content creator: 8-15 triệu/tháng | 299k - 1.3 triệu/tháng |
| Agency trọn gói: 15-50 triệu/tháng | Unlimited content |
| Thời gian: 10-20 giờ/tuần | 30 phút/tuần |
| Chất lượng: Không đều | Đồng nhất, đúng brand voice |

## 📁 Cấu trúc dự án

```
ai-content-agency/
├── docs/                           # Tài liệu chi tiết
│   ├── 01-TECH-STACK.md           # Kiến trúc hệ thống
│   ├── 02-PROMPT-TEMPLATES.md     # Prompt engineering
│   └── 04-GO-TO-MARKET-VIETNAM.md # Chiến lược GTM
│
├── src/
│   ├── backend/                    # FastAPI Backend
│   │   ├── app/
│   │   │   ├── api/               # API endpoints
│   │   │   ├── models/            # Database models
│   │   │   ├── schemas/           # Pydantic schemas
│   │   │   ├── services/          # Business logic
│   │   │   │   └── ai/            # AI generation services
│   │   │   ├── config.py          # Configuration
│   │   │   ├── database.py        # Database setup
│   │   │   └── main.py            # FastAPI app
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   └── .env.example
│   │
│   └── frontend/                   # Next.js Frontend
│       ├── app/
│       │   ├── page.tsx           # Landing page
│       │   └── dashboard/         # Dashboard UI
│       ├── lib/
│       │   └── api.ts             # API client
│       └── package.json
│
├── docker-compose.yml              # Docker orchestration
└── README.md
```

## 🚀 Quick Start

### 1. Clone repository

```bash
git clone <repository-url>
cd ai-content-agency
```

### 2. Setup Backend

```bash
cd src/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Edit .env with your API keys

# Run database migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

### 3. Setup Frontend

```bash
cd src/frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

### 4. Hoặc dùng Docker

```bash
# Copy env file
cp src/backend/.env.example src/backend/.env
# Edit with your API keys

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f
```

## 🔑 API Keys cần thiết

| Service | Mục đích | Link đăng ký |
|---------|----------|--------------|
| OpenAI | Text generation (GPT-4o) | [platform.openai.com](https://platform.openai.com) |
| Anthropic | Text generation (Claude) | [console.anthropic.com](https://console.anthropic.com) |
| Replicate | Image generation (Flux) | [replicate.com](https://replicate.com) |
| HeyGen | Video generation | [heygen.com](https://heygen.com) |
| ElevenLabs | Voice generation | [elevenlabs.io](https://elevenlabs.io) |

## 📚 Documentation

| Document | Nội dung |
|----------|----------|
| [01-TECH-STACK.md](docs/01-TECH-STACK.md) | Kiến trúc hệ thống, tech stack chi tiết |
| [02-PROMPT-TEMPLATES.md](docs/02-PROMPT-TEMPLATES.md) | Prompt engineering cho từng loại content |
| [04-GO-TO-MARKET-VIETNAM.md](docs/04-GO-TO-MARKET-VIETNAM.md) | Chiến lược GTM cho thị trường VN |

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 16
- **Cache/Queue**: Redis 7
- **Task Queue**: Celery
- **AI**: OpenAI GPT-4o, Anthropic Claude, Replicate

### Frontend
- **Framework**: Next.js 14 (App Router)
- **Styling**: Tailwind CSS
- **Components**: Shadcn/ui
- **State**: Zustand + React Query

### Infrastructure
- **Container**: Docker
- **Deployment**: Vercel (frontend), Railway (backend)
- **Storage**: Cloudflare R2 / AWS S3

## 📊 API Endpoints

### Authentication
```
POST /api/v1/auth/register    # Đăng ký
POST /api/v1/auth/login       # Đăng nhập
GET  /api/v1/auth/me          # User info
```

### Brands
```
POST   /api/v1/brands/        # Tạo brand
GET    /api/v1/brands/        # List brands
GET    /api/v1/brands/{id}    # Get brand
PUT    /api/v1/brands/{id}    # Update brand
DELETE /api/v1/brands/{id}    # Delete brand
```

### Content Generation
```
POST /api/v1/generate/content # Generate content
POST /api/v1/generate/image   # Generate image
POST /api/v1/generate/quick/{type} # Quick generate
```

### Content Management
```
POST   /api/v1/contents/      # Save content
GET    /api/v1/contents/      # List contents
GET    /api/v1/contents/{id}  # Get content
PATCH  /api/v1/contents/{id}/status # Update status
DELETE /api/v1/contents/{id}  # Delete content
```

## 💰 Pricing

| Tier | Giá | Features |
|------|-----|----------|
| Free | 0đ | 10 posts, 5 ads/tháng |
| Starter | 299k/tháng | 30 posts, 10 ads, 5 videos |
| Growth | 599k/tháng | 60 posts, 30 ads, 20 images |
| Scale | 1.299tr/tháng | Unlimited, dedicated support |

## 🗺️ Roadmap

### Phase 1 (Current)
- [x] Core text generation (Social, Ads, Landing, Video)
- [x] Basic image generation
- [x] User authentication
- [x] Brand management

### Phase 2
- [ ] Content scheduling & auto-posting
- [ ] Analytics dashboard
- [ ] A/B testing
- [ ] Team collaboration

### Phase 3
- [ ] Video generation với HeyGen
- [ ] Multi-language support
- [ ] API cho agencies
- [ ] Mobile app

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines first.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙋 Support

- 📧 Email: support@aicontentagency.vn
- 💬 Zalo OA: AI Content Agency
- 📘 Facebook Group: AI Content Marketing Vietnam

---

Made with ❤️ in Vietnam 🇻🇳
