'use client'

import { useState } from 'react'

// Types
interface ContentVariation {
  hook: string
  body: string
  cta: string
  hashtags: string[]
  image_suggestion?: string
}

interface GenerateResult {
  success: boolean
  content_type: string
  brand_name: string
  variations: ContentVariation[]
  ai_model_used: string
  tokens_used: { input_tokens: number; output_tokens: number }
  generation_time_seconds: number
}

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('generate')
  const [selectedContentType, setSelectedContentType] = useState('social_facebook')
  const [topic, setTopic] = useState('')
  const [isGenerating, setIsGenerating] = useState(false)
  const [result, setResult] = useState<GenerateResult | null>(null)

  const contentTypes = [
    { id: 'social_facebook', label: 'Facebook Post', icon: '📘' },
    { id: 'social_instagram', label: 'Instagram', icon: '📸' },
    { id: 'social_tiktok', label: 'TikTok', icon: '🎵' },
    { id: 'social_linkedin', label: 'LinkedIn', icon: '💼' },
    { id: 'ads_facebook', label: 'Facebook Ads', icon: '🎯' },
    { id: 'ads_google', label: 'Google Ads', icon: '🔍' },
    { id: 'landing_page', label: 'Landing Page', icon: '🏠' },
    { id: 'video_script', label: 'Video Script', icon: '🎬' },
  ]

  const handleGenerate = async () => {
    setIsGenerating(true)
    
    // Simulate API call - Replace with actual API call
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    // Mock result
    setResult({
      success: true,
      content_type: selectedContentType,
      brand_name: 'Demo Brand',
      variations: [
        {
          hook: 'Bạn có biết 80% doanh nghiệp thất bại vì điều này? 🤯',
          body: `Đó là THIẾU CHIẾN LƯỢC CONTENT rõ ràng!

Mình đã gặp hàng trăm chủ doanh nghiệp, và pattern luôn giống nhau:
✓ Đăng bài không đều
✓ Không biết đăng gì
✓ Copy đối thủ nhưng không hiệu quả

Giải pháp? Hệ thống hóa content với AI.

Một lần setup → Content tự động chạy mỗi ngày.
Không cần thuê team → Tiết kiệm 70% chi phí.
Chất lượng đồng đều → Brand identity mạnh hơn.`,
          cta: '💬 Comment "AI" để nhận tư vấn miễn phí!',
          hashtags: ['#ContentMarketing', '#AIMarketing', '#DigitalMarketing', '#BusinessTips'],
          image_suggestion: 'Infographic showing 80% statistic with before/after comparison'
        },
        {
          hook: '3 sai lầm content khiến bạn mất khách hàng mỗi ngày 😱',
          body: `Sai lầm #1: Đăng bài không có chiến lược
→ Khách không nhớ bạn là ai

Sai lầm #2: Content không đúng pain point
→ Khách không thấy lý do mua

Sai lầm #3: Không có hệ thống
→ Bạn kiệt sức, content đứt quãng

Fix ngay với AI Content Agency:
📌 Content calendar tự động
📌 Nội dung chuẩn brand voice
📌 Tiết kiệm 10+ giờ/tuần`,
          cta: '🔥 Link trong bio - Dùng thử miễn phí!',
          hashtags: ['#MarketingTips', '#ContentStrategy', '#SmallBusiness', '#GrowthHacking'],
          image_suggestion: 'Carousel with 3 slides, each showing one mistake'
        },
        {
          hook: 'Story time: Từ 0 đến 10k followers trong 30 ngày 📈',
          body: `Tháng trước page mình chỉ có 500 followers.
Hôm nay? 10,500+ và vẫn tăng.

Không phải may mắn. Không phải viral.
Mà là HỆ THỐNG.

Đây là công thức:
1️⃣ 1 pillar content/tuần (bài dài, giá trị cao)
2️⃣ 5 micro content/tuần (derived từ pillar)
3️⃣ 7 engagement content/tuần (poll, question, meme)

Tổng: 13 bài/tuần, nhưng chỉ cần sáng tạo 1 lần.

AI giúp mình:
- Viết 13 bài trong 30 phút
- Giữ đúng tone xuyên suốt
- Suggest hình ảnh matching`,
          cta: 'Save lại và theo dõi để xem kết quả tháng sau!',
          hashtags: ['#GrowthStory', '#SocialMediaGrowth', '#ContentCreator', '#MarketingAutomation'],
          image_suggestion: 'Before/after screenshot of follower count with growth chart'
        }
      ],
      ai_model_used: 'openai/gpt-4o',
      tokens_used: { input_tokens: 850, output_tokens: 1200 },
      generation_time_seconds: 3.2
    })
    
    setIsGenerating(false)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Sidebar */}
      <aside className="fixed left-0 top-0 h-full w-64 bg-white border-r p-4">
        <h1 className="text-xl font-bold text-blue-600 mb-8">🚀 AI Content</h1>
        
        <nav className="space-y-2">
          <SidebarItem 
            icon="⚡" 
            label="Generate" 
            active={activeTab === 'generate'} 
            onClick={() => setActiveTab('generate')}
          />
          <SidebarItem 
            icon="📁" 
            label="My Content" 
            active={activeTab === 'content'} 
            onClick={() => setActiveTab('content')}
          />
          <SidebarItem 
            icon="🏢" 
            label="Brands" 
            active={activeTab === 'brands'} 
            onClick={() => setActiveTab('brands')}
          />
          <SidebarItem 
            icon="📅" 
            label="Calendar" 
            active={activeTab === 'calendar'} 
            onClick={() => setActiveTab('calendar')}
          />
          <SidebarItem 
            icon="⚙️" 
            label="Settings" 
            active={activeTab === 'settings'} 
            onClick={() => setActiveTab('settings')}
          />
        </nav>

        {/* Usage Stats */}
        <div className="absolute bottom-4 left-4 right-4 bg-blue-50 rounded-lg p-4">
          <p className="text-sm font-medium text-blue-900">This month</p>
          <div className="mt-2 space-y-1">
            <UsageBar label="Social posts" used={8} limit={30} />
            <UsageBar label="Ads" used={3} limit={10} />
            <UsageBar label="Landing pages" used={1} limit={2} />
          </div>
          <button className="w-full mt-3 text-sm text-blue-600 font-medium hover:underline">
            Upgrade plan →
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="ml-64 p-8">
        <div className="max-w-6xl">
          {/* Header */}
          <div className="flex justify-between items-center mb-8">
            <div>
              <h2 className="text-2xl font-bold">Generate Content</h2>
              <p className="text-gray-600">Tạo content marketing với AI trong vài giây</p>
            </div>
            <div className="flex items-center gap-4">
              <select className="border rounded-lg px-4 py-2 bg-white">
                <option>Demo Brand</option>
                <option>+ Add new brand</option>
              </select>
            </div>
          </div>

          {/* Content Type Selection */}
          <div className="bg-white rounded-xl p-6 mb-6 shadow-sm">
            <h3 className="font-semibold mb-4">Chọn loại content</h3>
            <div className="grid grid-cols-4 gap-3">
              {contentTypes.map(type => (
                <button
                  key={type.id}
                  onClick={() => setSelectedContentType(type.id)}
                  className={`p-4 rounded-lg border-2 transition text-left ${
                    selectedContentType === type.id 
                      ? 'border-blue-600 bg-blue-50' 
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <span className="text-2xl">{type.icon}</span>
                  <p className="mt-2 font-medium text-sm">{type.label}</p>
                </button>
              ))}
            </div>
          </div>

          {/* Generation Form */}
          <div className="bg-white rounded-xl p-6 mb-6 shadow-sm">
            <h3 className="font-semibold mb-4">Thông tin content</h3>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Chủ đề / Topic
                </label>
                <input
                  type="text"
                  value={topic}
                  onChange={(e) => setTopic(e.target.value)}
                  placeholder="VD: Ra mắt sản phẩm mới, Tips sử dụng, Behind the scenes..."
                  className="w-full border rounded-lg px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Mục tiêu
                  </label>
                  <select className="w-full border rounded-lg px-4 py-3">
                    <option value="engagement">Tăng tương tác (Engagement)</option>
                    <option value="awareness">Tăng nhận diện (Awareness)</option>
                    <option value="conversion">Thúc đẩy mua hàng (Conversion)</option>
                    <option value="traffic">Tăng traffic</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Độ dài
                  </label>
                  <select className="w-full border rounded-lg px-4 py-3">
                    <option value="short">Ngắn (2-3 câu)</option>
                    <option value="medium">Trung bình (4-6 câu)</option>
                    <option value="long">Dài (7+ câu)</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Promotion (nếu có)
                </label>
                <input
                  type="text"
                  placeholder="VD: Giảm 30% đến hết tuần, Mua 1 tặng 1..."
                  className="w-full border rounded-lg px-4 py-3"
                />
              </div>
            </div>

            <button
              onClick={handleGenerate}
              disabled={isGenerating}
              className="mt-6 w-full bg-blue-600 text-white py-4 rounded-lg font-semibold hover:bg-blue-700 transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              {isGenerating ? (
                <>
                  <span className="animate-spin">⏳</span>
                  Đang tạo content...
                </>
              ) : (
                <>
                  ⚡ Generate 3 variations
                </>
              )}
            </button>
          </div>

          {/* Results */}
          {result && (
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h3 className="font-semibold">Kết quả ({result.variations.length} variations)</h3>
                <div className="text-sm text-gray-500">
                  {result.ai_model_used} • {result.generation_time_seconds}s • {result.tokens_used.output_tokens} tokens
                </div>
              </div>

              {result.variations.map((variation, index) => (
                <div key={index} className="bg-white rounded-xl p-6 shadow-sm">
                  <div className="flex justify-between items-start mb-4">
                    <span className="bg-blue-100 text-blue-700 text-sm font-medium px-3 py-1 rounded-full">
                      Variation {index + 1}
                    </span>
                    <div className="flex gap-2">
                      <button className="text-gray-500 hover:text-gray-700 p-2">
                        📋 Copy
                      </button>
                      <button className="text-gray-500 hover:text-gray-700 p-2">
                        💾 Save
                      </button>
                      <button className="text-gray-500 hover:text-gray-700 p-2">
                        ✏️ Edit
                      </button>
                    </div>
                  </div>

                  <div className="space-y-4">
                    <div>
                      <p className="text-xs text-gray-500 uppercase font-medium mb-1">Hook</p>
                      <p className="text-lg font-semibold text-blue-600">{variation.hook}</p>
                    </div>
                    
                    <div>
                      <p className="text-xs text-gray-500 uppercase font-medium mb-1">Body</p>
                      <p className="whitespace-pre-wrap text-gray-700">{variation.body}</p>
                    </div>

                    <div>
                      <p className="text-xs text-gray-500 uppercase font-medium mb-1">CTA</p>
                      <p className="font-medium text-green-600">{variation.cta}</p>
                    </div>

                    <div>
                      <p className="text-xs text-gray-500 uppercase font-medium mb-1">Hashtags</p>
                      <div className="flex flex-wrap gap-2">
                        {variation.hashtags.map((tag, i) => (
                          <span key={i} className="bg-gray-100 text-gray-600 text-sm px-2 py-1 rounded">
                            {tag}
                          </span>
                        ))}
                      </div>
                    </div>

                    {variation.image_suggestion && (
                      <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3">
                        <p className="text-xs text-yellow-700 uppercase font-medium mb-1">💡 Gợi ý hình ảnh</p>
                        <p className="text-sm text-yellow-800">{variation.image_suggestion}</p>
                        <button className="mt-2 text-sm text-yellow-700 font-medium hover:underline">
                          🖼️ Generate image with AI →
                        </button>
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  )
}

function SidebarItem({ icon, label, active, onClick }: {
  icon: string
  label: string
  active: boolean
  onClick: () => void
}) {
  return (
    <button
      onClick={onClick}
      className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition ${
        active 
          ? 'bg-blue-50 text-blue-600' 
          : 'text-gray-600 hover:bg-gray-50'
      }`}
    >
      <span>{icon}</span>
      <span className="font-medium">{label}</span>
    </button>
  )
}

function UsageBar({ label, used, limit }: { label: string; used: number; limit: number }) {
  const percentage = Math.min((used / limit) * 100, 100)
  return (
    <div>
      <div className="flex justify-between text-xs text-gray-600">
        <span>{label}</span>
        <span>{used}/{limit}</span>
      </div>
      <div className="h-1.5 bg-gray-200 rounded-full mt-1">
        <div 
          className="h-full bg-blue-600 rounded-full transition-all"
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  )
}
