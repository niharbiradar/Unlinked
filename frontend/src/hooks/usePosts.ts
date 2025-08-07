import { useState, useEffect, useCallback } from 'react';
import { postsApi, Post, CreatePostRequest } from '../services/api';

interface UsePostsReturn {
  posts: Post[];
  loading: boolean;
  error: string | null;
  createPost: (postData: CreatePostRequest) => Promise<void>;
  refreshPosts: () => Promise<void>;
  hasMore: boolean;
  loadMore: () => Promise<void>;
}

export const usePosts = (limit = 20): UsePostsReturn => {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [hasMore, setHasMore] = useState(true);
  const [skip, setSkip] = useState(0);

  const fetchPosts = useCallback(async (skipCount = 0, append = false) => {
    try {
      setError(null);
      const fetchedPosts = await postsApi.getPosts(skipCount, limit);
      
      if (append) {
        setPosts(prev => [...prev, ...fetchedPosts]);
      } else {
        setPosts(fetchedPosts);
      }
      
      setHasMore(fetchedPosts.length === limit);
      setSkip(skipCount + fetchedPosts.length);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to fetch posts';
      setError(errorMessage);
      console.error('Error fetching posts:', err);
    } finally {
      setLoading(false);
    }
  }, [limit]);

  const createPost = useCallback(async (postData: CreatePostRequest) => {
    try {
      setError(null);
      const newPost = await postsApi.createPost(postData);
      setPosts(prev => [newPost, ...prev]);
      return Promise.resolve();
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to create post';
      setError(errorMessage);
      console.error('Error creating post:', err);
      return Promise.reject(err);
    }
  }, []);

  const refreshPosts = useCallback(async () => {
    setLoading(true);
    setSkip(0);
    await fetchPosts(0, false);
  }, [fetchPosts]);

  const loadMore = useCallback(async () => {
    if (!loading && hasMore) {
      await fetchPosts(skip, true);
    }
  }, [loading, hasMore, skip, fetchPosts]);

  // Initial load
  useEffect(() => {
    fetchPosts(0, false);
  }, [fetchPosts]);

  return {
    posts,
    loading,
    error,
    createPost,
    refreshPosts,
    hasMore,
    loadMore,
  };
}; 