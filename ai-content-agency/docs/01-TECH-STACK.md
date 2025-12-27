# 🛠️ PHẦN 1: TECH STACK CHI TIẾT

## Tổng quan kiến trúc

```
┌────────────────────────────────────────────────────────────────────────────┐
│                           FRONTEND LAYER                                    │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │   Next.js 14    │  │   Tailwind CSS  │  │   Shadcn/ui     │            │
│  │   (App Router)  │  │   (Styling)     │  │   (Components)  │            │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘            │
└────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ REST API / WebSocket
                                    ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                           BACKEND LAYER                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │   FastAPI       │  │   Celery        │  │   Redis         │            │
│  │   (API Server)  │  │   (Task Queue)  │  │   (Cache/Queue) │            │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │   PostgreSQL    │  │   Supabase      │  │   S3/R2         │            │
│  │   (Database)    │  │   (Auth/BaaS)   │  │   (Storage)     │            │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘            │
└────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ API Calls
                                    ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                           AI SERVICES LAYER                                 │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                        TEXT GENERATION                               │  │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐        │  │
│  │  │ OpenAI    │  │ Anthropic │  │ Groq      │  │ Together  │        │  │
│  │  │ GPT-4o    │  │ Claude    │  │ (Fast)    │  │ (Cheap)   │        │  │
│  │  └───────────┘  └───────────┘  └───────────┘  └───────────┘        │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                        IMAGE GENERATION                              │  │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐        │  │
│  │  │ DALL-E 3  │  │ Midjourney│  │ Flux      │  │ Leonardo  │        │  │
│  │  │ (OpenAI)  │  │ (Discord) │  │(Replicate)│  │ (API)     │        │  │
│  │  └───────────┘  └───────────┘  └───────────┘  └───────────┘        │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                        VIDEO & AUDIO                                 │  │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐        │  │
│  │  │ HeyGen    │  │ Runway    │  │ ElevenLabs│  │ Synthesia │        │  │
│  │  │ (Avatar)  │  │ (Gen-3)   │  │ (Voice)   │  │ (Avatar)  │        │  │
│  │  └───────────┘  └───────────┘  └───────────┘  └───────────┘        │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Webhooks / Scheduling
                                    ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                        DISTRIBUTION LAYER                                   │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐              │
│  │ Facebook  │  │ Instagram │  │ TikTok    │  │ LinkedIn  │              │
│  │ Graph API │  │ Graph API │  │ API       │  │ API       │              │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘              │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 📦 Chi tiết từng thành phần

### 1. FRONTEND

#### 1.1 Next.js 14 (App Router)
```bash
# Khởi tạo project
npx create-next-app@latest ai-content-agency --typescript --tailwind --app --src-dir

# Dependencies chính
npm install @tanstack/react-query axios zustand
npm install @radix-ui/react-* # Shadcn components
npm install date-fns recharts # Utils & Charts
npm install react-hook-form zod @hookform/resolvers # Forms
```

**Tại sao chọn Next.js 14:**
- Server Components = load nhanh hơn
- App Router = routing hiện đại
- Built-in API Routes = không cần backend riêng cho simple tasks
- Vercel deploy = 1 click

#### 1.2 Shadcn/ui
```bash
# Setup
npx shadcn-ui@latest init

# Components cần thiết
npx shadcn-ui@latest add button card dialog form input
npx shadcn-ui@latest add select tabs textarea toast avatar
npx shadcn-ui@latest add dropdown-menu sidebar calendar
```

**Components chính cho Dashboard:**
- `Sidebar` - Navigation
- `Card` - Content display
- `Dialog` - Modals
- `Form` - Input forms
- `Calendar` - Content scheduling

#### 1.3 State Management
```typescript
// Zustand store example
import { create } from 'zustand'

interface BrandStore {
  currentBrand: Brand | null
  setBrand: (brand: Brand) => void
  contents: Content[]
  addContent: (content: Content) => void
}

export const useBrandStore = create<BrandStore>((set) => ({
  currentBrand: null,
  setBrand: (brand) => set({ currentBrand: brand }),
  contents: [],
  addContent: (content) => set((state) => ({ 
    contents: [...state.contents, content] 
  })),
}))
```

---

### 2. BACKEND

#### 2.1 FastAPI (Python)
```bash
# Dependencies
pip install fastapi uvicorn sqlalchemy alembic
pip install celery redis
pip install openai anthropic replicate
pip install python-multipart pydantic-settings
pip install supabase python-jose passlib
```

**Cấu trúc project:**
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app
│   ├── config.py            # Settings
│   ├── database.py          # DB connection
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py          # Dependencies
│   │   ├── v1/
│   │   │   ├── brands.py    # Brand endpoints
│   │   │   ├── contents.py  # Content endpoints
│   │   │   ├── generate.py  # AI generation
│   │   │   └── auth.py      # Authentication
│   │
│   ├── models/
│   │   ├── brand.py
│   │   ├── content.py
│   │   └── user.py
│   │
│   ├── schemas/
│   │   ├── brand.py
│   │   ├── content.py
│   │   └── generate.py
│   │
│   ├── services/
│   │   ├── ai/
│   │   │   ├── text_generator.py
│   │   │   ├── image_generator.py
│   │   │   └── video_generator.py
│   │   ├── social/
│   │   │   ├── facebook.py
│   │   │   └── instagram.py
│   │   └── storage.py
│   │
│   └── workers/
│       ├── celery_app.py
│       └── tasks.py
│
├── alembic/                 # Migrations
├── tests/
├── requirements.txt
└── Dockerfile
```

#### 2.2 Database Schema (PostgreSQL)
```sql
-- Brands table
CREATE TABLE brands (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    industry VARCHAR(100),
    description TEXT,
    tone_of_voice VARCHAR(50), -- professional, friendly, casual
    target_audience JSONB,
    brand_colors JSONB,
    logo_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Products table
CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    brand_id UUID REFERENCES brands(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    features JSONB,
    benefits JSONB,
    price DECIMAL(10,2),
    images JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Contents table
CREATE TABLE contents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    brand_id UUID REFERENCES brands(id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL, -- social, ads, landing, video
    platform VARCHAR(50), -- facebook, instagram, tiktok, google
    title VARCHAR(500),
    body TEXT,
    media_urls JSONB,
    hashtags TEXT[],
    cta VARCHAR(255),
    status VARCHAR(20) DEFAULT 'draft', -- draft, approved, scheduled, published
    scheduled_at TIMESTAMP,
    published_at TIMESTAMP,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Content Versions (for A/B testing)
CREATE TABLE content_versions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content_id UUID REFERENCES contents(id) ON DELETE CASCADE,
    version_name VARCHAR(50),
    body TEXT,
    performance_score DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Prompts Library
CREATE TABLE prompts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    category VARCHAR(50), -- social, ads, landing, video
    template TEXT NOT NULL,
    variables JSONB, -- required variables
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### 2.3 Celery (Background Tasks)
```python
# workers/celery_app.py
from celery import Celery

celery_app = Celery(
    "ai_content_agency",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Ho_Chi_Minh",
    enable_utc=True,
    task_routes={
        "workers.tasks.generate_content": {"queue": "content"},
        "workers.tasks.generate_image": {"queue": "image"},
        "workers.tasks.publish_content": {"queue": "publish"},
    }
)
```

```python
# workers/tasks.py
from celery_app import celery_app
from services.ai import TextGenerator, ImageGenerator

@celery_app.task(bind=True, max_retries=3)
def generate_content(self, brand_id: str, content_type: str, params: dict):
    try:
        generator = TextGenerator()
        result = generator.generate(brand_id, content_type, params)
        return result
    except Exception as e:
        self.retry(countdown=60, exc=e)

@celery_app.task(bind=True, max_retries=3)
def generate_image(self, prompt: str, style: str, size: str):
    try:
        generator = ImageGenerator()
        result = generator.generate(prompt, style, size)
        return result
    except Exception as e:
        self.retry(countdown=60, exc=e)

@celery_app.task
def schedule_publish(content_id: str, platform: str, scheduled_time: str):
    # Logic to publish content at scheduled time
    pass
```

---

### 3. AI SERVICES

#### 3.1 Text Generation - Multi-Provider Strategy

```python
# services/ai/text_generator.py
from abc import ABC, abstractmethod
from openai import OpenAI
from anthropic import Anthropic
import os

class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, system: str) -> str:
        pass

class OpenAIProvider(LLMProvider):
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def generate(self, prompt: str, system: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content

class AnthropicProvider(LLMProvider):
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    def generate(self, prompt: str, system: str) -> str:
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            system=system,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

class TextGenerator:
    def __init__(self, provider: str = "openai"):
        providers = {
            "openai": OpenAIProvider,
            "anthropic": AnthropicProvider,
        }
        self.provider = providers[provider]()
    
    def generate_social_post(self, brand_context: dict, params: dict) -> dict:
        system = self._build_system_prompt("social", brand_context)
        prompt = self._build_user_prompt("social", params)
        
        result = self.provider.generate(prompt, system)
        return self._parse_output(result, "social")
    
    def generate_ads_copy(self, brand_context: dict, params: dict) -> dict:
        system = self._build_system_prompt("ads", brand_context)
        prompt = self._build_user_prompt("ads", params)
        
        result = self.provider.generate(prompt, system)
        return self._parse_output(result, "ads")
```

#### 3.2 Image Generation

```python
# services/ai/image_generator.py
from openai import OpenAI
import replicate
import os

class ImageGenerator:
    def __init__(self):
        self.openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def generate_dalle(self, prompt: str, size: str = "1024x1024") -> str:
        """DALL-E 3 - Best for product mockups, clean designs"""
        response = self.openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality="hd",
            n=1
        )
        return response.data[0].url
    
    def generate_flux(self, prompt: str, aspect_ratio: str = "1:1") -> str:
        """Flux - Best for photorealistic, artistic styles"""
        output = replicate.run(
            "black-forest-labs/flux-1.1-pro",
            input={
                "prompt": prompt,
                "aspect_ratio": aspect_ratio,
                "output_format": "webp",
                "output_quality": 90
            }
        )
        return output
    
    def generate_with_reference(self, prompt: str, reference_url: str) -> str:
        """Generate image with style reference"""
        output = replicate.run(
            "tencentarc/photomaker-style",
            input={
                "prompt": prompt,
                "input_image": reference_url,
                "style_strength_ratio": 30
            }
        )
        return output

# Prompt builder for marketing images
class MarketingImagePrompts:
    @staticmethod
    def product_showcase(product_name: str, style: str, background: str) -> str:
        return f"""Professional product photography of {product_name}.
Style: {style}
Background: {background}
Lighting: Soft studio lighting
Composition: Centered, rule of thirds
Quality: 8K, ultra detailed, commercial photography"""

    @staticmethod
    def social_media_post(theme: str, brand_colors: list, mood: str) -> str:
        colors_str = ", ".join(brand_colors)
        return f"""Social media post design.
Theme: {theme}
Brand colors: {colors_str}
Mood: {mood}
Style: Modern, minimalist, professional
Text space: Leave 30% space for text overlay
Aspect ratio: 1:1 for Instagram, 9:16 for Stories"""

    @staticmethod
    def ads_banner(product: str, headline: str, cta: str) -> str:
        return f"""Digital advertising banner design.
Product: {product}
Space for headline: "{headline}"
Space for CTA button: "{cta}"
Style: Clean, high-converting, attention-grabbing
Colors: Vibrant with high contrast
Layout: Product on left, text space on right"""
```

#### 3.3 Video Generation

```python
# services/ai/video_generator.py
import requests
import os

class VideoGenerator:
    def __init__(self):
        self.heygen_key = os.getenv("HEYGEN_API_KEY")
        self.elevenlabs_key = os.getenv("ELEVENLABS_API_KEY")
    
    def generate_avatar_video(
        self, 
        script: str, 
        avatar_id: str = "default",
        voice_id: str = "default"
    ) -> dict:
        """Generate talking head video with HeyGen"""
        
        url = "https://api.heygen.com/v2/video/generate"
        
        payload = {
            "video_inputs": [{
                "character": {
                    "type": "avatar",
                    "avatar_id": avatar_id,
                    "avatar_style": "normal"
                },
                "voice": {
                    "type": "text",
                    "input_text": script,
                    "voice_id": voice_id
                }
            }],
            "dimension": {"width": 1080, "height": 1920},  # 9:16 for TikTok/Reels
            "aspect_ratio": "9:16"
        }
        
        headers = {
            "X-Api-Key": self.heygen_key,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    
    def generate_voiceover(self, text: str, voice_id: str) -> bytes:
        """Generate voiceover with ElevenLabs"""
        
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        
        payload = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
        
        headers = {
            "xi-api-key": self.elevenlabs_key,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        return response.content
```

---

### 4. INFRASTRUCTURE & DEPLOYMENT

#### 4.1 Docker Compose (Development)
```yaml
# docker-compose.yml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/ai_agency
      - REDIS_URL=redis://redis:6379/0
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    depends_on:
      - db
      - redis
    volumes:
      - ./backend:/app

  celery_worker:
    build: ./backend
    command: celery -A workers.celery_app worker -l info -Q content,image,publish
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/ai_agency
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

  celery_beat:
    build: ./backend
    command: celery -A workers.celery_app beat -l info
    depends_on:
      - redis

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000
    volumes:
      - ./frontend:/app
      - /app/node_modules

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=ai_agency
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

#### 4.2 Production Deployment Options

```yaml
# Option 1: Railway.app (Recommended for MVP)
# Pros: Easy, auto-scaling, good pricing
# Deploy: Connect GitHub repo, auto-deploy

# Option 2: Vercel + Supabase + Railway
# - Frontend: Vercel (free tier good)
# - Database: Supabase (PostgreSQL + Auth)
# - Backend: Railway
# - Redis: Upstash (serverless Redis)

# Option 3: AWS (Scale)
# - ECS/Fargate for containers
# - RDS for PostgreSQL
# - ElastiCache for Redis
# - S3 for storage
# - CloudFront for CDN
```

#### 4.3 Environment Variables
```bash
# .env.example

# Database
DATABASE_URL=postgresql://user:pass@host:5432/db
REDIS_URL=redis://localhost:6379/0

# AI Services
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
REPLICATE_API_TOKEN=r8_...
HEYGEN_API_KEY=...
ELEVENLABS_API_KEY=...

# Storage
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
S3_BUCKET_NAME=ai-agency-assets

# Auth (Supabase)
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_KEY=...

# Social Media APIs
FACEBOOK_APP_ID=...
FACEBOOK_APP_SECRET=...
INSTAGRAM_ACCESS_TOKEN=...
```

---

### 5. CHI PHÍ ƯỚC TÍNH

#### 5.1 AI Services (Per 1000 requests)

| Service | Cost | Use case |
|---------|------|----------|
| GPT-4o | ~$5-10 | Text generation |
| Claude 3.5 | ~$3-8 | Long-form content |
| DALL-E 3 | ~$40 (1000 images) | Product images |
| Flux Pro | ~$40 (1000 images) | Marketing visuals |
| HeyGen | ~$30/video | Avatar videos |
| ElevenLabs | ~$5/100k chars | Voiceovers |

#### 5.2 Infrastructure (Monthly)

| Service | Cost | Notes |
|---------|------|-------|
| Vercel Pro | $20 | Frontend hosting |
| Railway | $20-50 | Backend + Workers |
| Supabase Pro | $25 | Database + Auth |
| Upstash | $10 | Redis |
| Cloudflare R2 | $5-20 | Storage |
| **Total** | **$80-125/month** | MVP infrastructure |

#### 5.3 Break-even Analysis

```
Fixed costs: ~$100/month (infrastructure)
Variable costs: ~$0.05-0.10 per content piece

Pricing: $299/month = 30 posts + 10 ads
Cost per client: $100/30 = ~$3.33 infrastructure + $2 AI = $5.33
Margin per client: $299 - $100 (your time) - $50 (AI) = ~$149 profit

Break-even: 1 client covers infrastructure
10 clients = ~$1,500/month profit
```

---

## 🔧 Quick Start Commands

```bash
# 1. Clone và setup
git clone <repo>
cd ai-content-agency

# 2. Setup backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env với API keys

# 3. Setup database
docker-compose up -d db redis
alembic upgrade head

# 4. Run backend
uvicorn app.main:app --reload

# 5. Setup frontend (new terminal)
cd frontend
npm install
npm run dev

# 6. Run Celery workers (new terminal)
celery -A workers.celery_app worker -l info
```

---

*Tiếp theo: Phần 2 - Prompt Templates chi tiết*
