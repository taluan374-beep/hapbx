/**
 * API Client for AI Content Agency
 */

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

interface ApiOptions {
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH'
  body?: any
  headers?: Record<string, string>
}

class ApiClient {
  private baseUrl: string
  private token: string | null = null

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl
    // Get token from localStorage if available
    if (typeof window !== 'undefined') {
      this.token = localStorage.getItem('token')
    }
  }

  setToken(token: string) {
    this.token = token
    if (typeof window !== 'undefined') {
      localStorage.setItem('token', token)
    }
  }

  clearToken() {
    this.token = null
    if (typeof window !== 'undefined') {
      localStorage.removeItem('token')
    }
  }

  private async request<T>(endpoint: string, options: ApiOptions = {}): Promise<T> {
    const { method = 'GET', body, headers = {} } = options

    const requestHeaders: Record<string, string> = {
      'Content-Type': 'application/json',
      ...headers,
    }

    if (this.token) {
      requestHeaders['Authorization'] = `Bearer ${this.token}`
    }

    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method,
      headers: requestHeaders,
      body: body ? JSON.stringify(body) : undefined,
    })

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: 'An error occurred' }))
      throw new Error(error.detail || `HTTP error ${response.status}`)
    }

    return response.json()
  }

  // Auth
  async register(email: string, password: string, fullName?: string) {
    const data = await this.request<{ access_token: string; user: any }>('/api/v1/auth/register', {
      method: 'POST',
      body: { email, password, full_name: fullName },
    })
    this.setToken(data.access_token)
    return data
  }

  async login(email: string, password: string) {
    const data = await this.request<{ access_token: string; user: any }>('/api/v1/auth/login', {
      method: 'POST',
      body: { email, password },
    })
    this.setToken(data.access_token)
    return data
  }

  async getMe() {
    return this.request<any>('/api/v1/auth/me')
  }

  // Brands
  async createBrand(brandData: any) {
    return this.request<any>('/api/v1/brands/', {
      method: 'POST',
      body: brandData,
    })
  }

  async listBrands() {
    return this.request<any[]>('/api/v1/brands/')
  }

  async getBrand(brandId: string) {
    return this.request<any>(`/api/v1/brands/${brandId}`)
  }

  async updateBrand(brandId: string, brandData: any) {
    return this.request<any>(`/api/v1/brands/${brandId}`, {
      method: 'PUT',
      body: brandData,
    })
  }

  async deleteBrand(brandId: string) {
    return this.request<void>(`/api/v1/brands/${brandId}`, {
      method: 'DELETE',
    })
  }

  // Content Generation
  async generateContent(params: {
    brand_id: string
    content_type: string
    topic?: string
    product_name?: string
    objective?: string
    key_message?: string
    promotion?: string
    num_variations?: number
    body_length?: string
    ai_provider?: string
  }) {
    return this.request<{
      success: boolean
      content_type: string
      brand_name: string
      variations: any[]
      ai_model_used: string
      tokens_used: { input_tokens: number; output_tokens: number }
      generation_time_seconds: number
    }>('/api/v1/generate/content', {
      method: 'POST',
      body: params,
    })
  }

  async generateImage(params: {
    brand_id: string
    prompt?: string
    auto_generate_prompt?: boolean
    image_type?: string
    style?: string
    aspect_ratio?: string
    provider?: string
  }) {
    return this.request<{
      success: boolean
      provider: string
      image_url: string
      prompt_used: string
    }>('/api/v1/generate/image', {
      method: 'POST',
      body: params,
    })
  }

  async quickGenerate(contentType: string, brandId: string, topic: string) {
    return this.request<any>(`/api/v1/generate/quick/${contentType}?brand_id=${brandId}&topic=${encodeURIComponent(topic)}`, {
      method: 'POST',
    })
  }

  // Contents
  async saveContent(contentData: any) {
    return this.request<any>('/api/v1/contents/', {
      method: 'POST',
      body: contentData,
    })
  }

  async listContents(params?: {
    brand_id?: string
    content_type?: string
    status?: string
    page?: number
    page_size?: number
  }) {
    const queryParams = new URLSearchParams()
    if (params?.brand_id) queryParams.set('brand_id', params.brand_id)
    if (params?.content_type) queryParams.set('content_type', params.content_type)
    if (params?.status) queryParams.set('status', params.status)
    if (params?.page) queryParams.set('page', params.page.toString())
    if (params?.page_size) queryParams.set('page_size', params.page_size.toString())

    const query = queryParams.toString()
    return this.request<{ items: any[]; total: number; page: number; page_size: number }>(
      `/api/v1/contents/${query ? `?${query}` : ''}`
    )
  }

  async getContent(contentId: string) {
    return this.request<any>(`/api/v1/contents/${contentId}`)
  }

  async updateContentStatus(contentId: string, status: string) {
    return this.request<any>(`/api/v1/contents/${contentId}/status?new_status=${status}`, {
      method: 'PATCH',
    })
  }

  async deleteContent(contentId: string) {
    return this.request<void>(`/api/v1/contents/${contentId}`, {
      method: 'DELETE',
    })
  }

  async duplicateContent(contentId: string) {
    return this.request<any>(`/api/v1/contents/${contentId}/duplicate`, {
      method: 'POST',
    })
  }
}

export const api = new ApiClient(API_URL)

// React Query hooks
export const queryKeys = {
  brands: ['brands'] as const,
  brand: (id: string) => ['brands', id] as const,
  contents: (params?: any) => ['contents', params] as const,
  content: (id: string) => ['contents', id] as const,
  user: ['user'] as const,
}
