import React from 'react';
import Layout from './components/Layout/Layout';
import PostForm from './components/Post/PostForm';
import Feed from './components/Feed/Feed';
import { usePosts } from './hooks/usePosts';

function App() {
  const { 
    posts, 
    loading, 
    error, 
    createPost, 
    hasMore, 
    loadMore 
  } = usePosts(20);

  const handlePostSubmit = async (postData: { content: string; tags: string[] }) => {
    await createPost(postData);
  };

  return (
    <Layout>
      <div className="max-w-2xl mx-auto">
        {/* Post Form */}
        <PostForm onSubmit={handlePostSubmit} isSubmitting={loading} />
        
        {/* Feed */}
        <Feed 
          posts={posts} 
          isLoading={loading} 
          error={error}
          hasMore={hasMore}
          onLoadMore={loadMore}
        />
      </div>
    </Layout>
  );
}

export default App;
