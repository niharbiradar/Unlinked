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
    <div className="card mb-6">
      {/* Post content */}
      <div className="mb-4">
        <p className="text-gray-900 leading-relaxed">{post.content}</p>
      </div>

      {/* Tags */}
      {post.tags.length > 0 && (
        <div className="flex flex-wrap gap-2 mb-4">
          {post.tags.map((tag, index) => (
            <span
              key={index}
              className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-primary-100 text-primary-800"
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
            <button className="flex items-center space-x-1 text-gray-500 hover:text-primary-600 transition-colors duration-200">
              <HeartIcon className="h-4 w-4" />
              <span className="text-sm">{post.reaction_counts.same}</span>
            </button>
            <button className="flex items-center space-x-1 text-gray-500 hover:text-primary-600 transition-colors duration-200">
              <HandThumbUpIcon className="h-4 w-4" />
              <span className="text-sm">{post.reaction_counts.helpful}</span>
            </button>
            <button className="flex items-center space-x-1 text-gray-500 hover:text-primary-600 transition-colors duration-200">
              <ChatBubbleLeftIcon className="h-4 w-4" />
              <span className="text-sm">{post.reaction_counts.upvote}</span>
            </button>
          </div>
        </div>

        {/* Timestamp */}
        <div className="text-sm text-gray-500">
          {formatDate(post.created_at)}
        </div>
      </div>
    </div>
  );
};

export default PostCard; 