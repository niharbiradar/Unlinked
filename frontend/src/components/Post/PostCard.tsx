import React from 'react';
import { HeartIcon, HandThumbUpIcon, ChatBubbleLeftIcon } from '@heroicons/react/24/outline';
import { Post } from '../../services/api';

interface PostCardProps {
  post: Post;
}

const PostCard: React.FC<PostCardProps> = ({ post }) => {
  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    const now = new Date();
    const diffInHours = Math.floor((now.getTime() - date.getTime()) / (1000 * 60 * 60));
    
    if (diffInHours < 1) return 'Just now';
    if (diffInHours < 24) return `${diffInHours}h ago`;
    return date.toLocaleDateString();
  };

  return (
    <div className="card mb-6 animate-fade-in">
      {/* Post content */}
      <div className="mb-4">
        <p className="text-gray-100 leading-relaxed text-base">{post.content}</p>
      </div>

      {/* Tags */}
      {post.tags.length > 0 && (
        <div className="flex flex-wrap gap-2 mb-4">
          {post.tags.map((tag, index) => (
            <span
              key={index}
              className="tag-modern"
            >
              #{tag}
            </span>
          ))}
        </div>
      )}

      {/* Post metadata and reactions */}
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-4">
          {/* Reactions */}
          <div className="flex items-center space-x-4">
            <button className="reaction-btn">
              <HeartIcon className="h-4 w-4" />
              <span className="text-sm font-medium">{post.reaction_counts.same}</span>
            </button>
            <button className="reaction-btn">
              <HandThumbUpIcon className="h-4 w-4" />
              <span className="text-sm font-medium">{post.reaction_counts.helpful}</span>
            </button>
            <button className="reaction-btn">
              <ChatBubbleLeftIcon className="h-4 w-4" />
              <span className="text-sm font-medium">{post.reaction_counts.upvote}</span>
            </button>
          </div>
        </div>

        {/* Timestamp */}
        <div className="text-sm text-gray-400">
          {formatDate(post.created_at)}
        </div>
      </div>
    </div>
  );
};

export default PostCard; 