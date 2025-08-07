import axios from 'axios';

// API configuration
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging and error handling
api.interceptors.request.use(
  (config) => {
    console.log(`Making ${config.method?.toUpperCase()} request to ${config.url}`);
    return config;
  },
  (error) => {
    console.error('Request error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.error('Response error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// Types
export interface Post {
  id: string;
  content: string;
  tags: string[];
  created_at: string;
  is_flagged: boolean;
  reaction_counts: {
    same: number;
    helpful: number;
    upvote: number;
  };
}

export interface CreatePostRequest {
  content: string;
  tags: string[];
  is_private?: boolean;
}

// API functions
export const postsApi = {
  // Get all posts
  getPosts: async (skip = 0, limit = 20, tag?: string): Promise<Post[]> => {
    const params = new URLSearchParams();
    if (skip > 0) params.append('skip', skip.toString());
    if (limit !== 20) params.append('limit', limit.toString());
    if (tag) params.append('tag', tag);
    
    const response = await api.get(`/posts?${params.toString()}`);
    return response.data;
  },

  // Get a specific post
  getPost: async (postId: string): Promise<Post> => {
    const response = await api.get(`/posts/${postId}`);
    return response.data;
  },

  // Create a new post
  createPost: async (postData: CreatePostRequest): Promise<Post> => {
    const response = await api.post('/posts/', postData);
    return response.data;
  },
};

export default api; 