'use client'

import { useState } from 'react'
import Link from 'next/link'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <header className="border-b bg-white/80 backdrop-blur-sm">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-blue-600">🚀 AI Content Agency</h1>
          <div className="space-x-4">
            <Link href="/login" className="text-gray-600 hover:text-gray-900">
              Đăng nhập
            </Link>
            <Link 
              href="/register" 
              className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
            >
              Đăng ký miễn phí
            </Link>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <main className="container mx-auto px-4 py-16">
        <div className="text-center max-w-4xl mx-auto">
          <h2 className="text-5xl font-bold text-gray-900 mb-6">
            Tạo Content Marketing
            <span className="text-blue-600"> Tự Động </span>
            với AI
          </h2>
          <p className="text-xl text-gray-600 mb-8">
            Tiết kiệm 70% thời gian và chi phí content. Tạo Social Posts, Ads Copy, 
            Landing Pages, Video Scripts chỉ với vài click.
          </p>
          <div className="flex justify-center gap-4">
            <Link 
              href="/register"
              className="bg-blue-600 text-white px-8 py-4 rounded-xl text-lg font-semibold hover:bg-blue-700 transition shadow-lg"
            >
              Bắt đầu miễn phí →
            </Link>
            <Link 
              href="/demo"
              className="bg-white text-gray-700 px-8 py-4 rounded-xl text-lg font-semibold hover:bg-gray-50 transition border"
            >
              Xem Demo
            </Link>
          </div>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mt-20">
          <FeatureCard 
            icon="📱"
            title="Social Content"
            description="Facebook, Instagram, TikTok, LinkedIn - Tạo posts tối ưu cho từng platform"
          />
          <FeatureCard 
            icon="🎯"
            title="Ads Copy"
            description="Facebook Ads, Google Ads, TikTok Ads với multiple variations cho A/B testing"
          />
          <FeatureCard 
            icon="🏠"
            title="Landing Pages"
            description="Copy hoàn chỉnh cho landing pages với CRO best practices"
          />
          <FeatureCard 
            icon="🎬"
            title="Video Scripts"
            description="Scripts cho TikTok, Reels, YouTube với timestamps chi tiết"
          />
        </div>

        {/* How it works */}
        <div className="mt-24">
          <h3 className="text-3xl font-bold text-center mb-12">Cách hoạt động</h3>
          <div className="grid md:grid-cols-3 gap-8">
            <StepCard 
              step={1}
              title="Nhập thông tin Brand"
              description="Điền thông tin thương hiệu, sản phẩm, đối tượng khách hàng một lần duy nhất"
            />
            <StepCard 
              step={2}
              title="Chọn loại content"
              description="Social post, ads, landing page hay video script - chọn và customize"
            />
            <StepCard 
              step={3}
              title="Nhận content ngay"
              description="AI tạo multiple variations trong vài giây, sẵn sàng sử dụng"
            />
          </div>
        </div>

        {/* Pricing Preview */}
        <div className="mt-24 text-center">
          <h3 className="text-3xl font-bold mb-4">Giá cả minh bạch</h3>
          <p className="text-gray-600 mb-8">Bắt đầu miễn phí, nâng cấp khi cần</p>
          
          <div className="grid md:grid-cols-3 gap-6 max-w-4xl mx-auto">
            <PricingCard 
              name="Free"
              price="0đ"
              features={[
                "10 social posts/tháng",
                "5 ads copies/tháng",
                "1 landing page/tháng",
                "Email support"
              ]}
            />
            <PricingCard 
              name="Starter"
              price="299k"
              popular
              features={[
                "30 social posts/tháng",
                "10 ads copies/tháng",
                "2 landing pages/tháng",
                "5 video scripts/tháng",
                "Priority support"
              ]}
            />
            <PricingCard 
              name="Growth"
              price="599k"
              features={[
                "60 social posts/tháng",
                "30 ads copies/tháng",
                "5 landing pages/tháng",
                "10 video scripts/tháng",
                "20 AI images/tháng",
                "Dedicated support"
              ]}
            />
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12 mt-24">
        <div className="container mx-auto px-4 text-center">
          <p className="text-gray-400">© 2024 AI Content Agency. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

function FeatureCard({ icon, title, description }: { icon: string; title: string; description: string }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-sm hover:shadow-md transition">
      <div className="text-4xl mb-4">{icon}</div>
      <h4 className="text-lg font-semibold mb-2">{title}</h4>
      <p className="text-gray-600 text-sm">{description}</p>
    </div>
  )
}

function StepCard({ step, title, description }: { step: number; title: string; description: string }) {
  return (
    <div className="text-center">
      <div className="w-12 h-12 bg-blue-600 text-white rounded-full flex items-center justify-center text-xl font-bold mx-auto mb-4">
        {step}
      </div>
      <h4 className="text-xl font-semibold mb-2">{title}</h4>
      <p className="text-gray-600">{description}</p>
    </div>
  )
}

function PricingCard({ name, price, features, popular }: { 
  name: string; 
  price: string; 
  features: string[];
  popular?: boolean;
}) {
  return (
    <div className={`bg-white p-6 rounded-xl ${popular ? 'ring-2 ring-blue-600 shadow-lg' : 'shadow-sm'}`}>
      {popular && (
        <span className="bg-blue-600 text-white text-xs px-3 py-1 rounded-full">Phổ biến</span>
      )}
      <h4 className="text-xl font-semibold mt-4">{name}</h4>
      <p className="text-3xl font-bold my-4">{price}<span className="text-sm font-normal text-gray-500">/tháng</span></p>
      <ul className="text-left space-y-2">
        {features.map((feature, i) => (
          <li key={i} className="flex items-center text-sm text-gray-600">
            <span className="text-green-500 mr-2">✓</span>
            {feature}
          </li>
        ))}
      </ul>
      <button className={`w-full mt-6 py-2 rounded-lg font-semibold transition ${
        popular 
          ? 'bg-blue-600 text-white hover:bg-blue-700' 
          : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
      }`}>
        Bắt đầu ngay
      </button>
    </div>
  )
}
