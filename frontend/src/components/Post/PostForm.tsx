import React, { useState } from 'react';
import { PaperAirplaneIcon } from '@heroicons/react/24/outline';
import { CreatePostRequest } from '../../services/api';

interface PostFormProps {
  onSubmit?: (post: CreatePostRequest) => Promise<void>;
  isSubmitting?: boolean;
}

const PostForm: React.FC<PostFormProps> = ({ onSubmit, isSubmitting = false }) => {
  const [content, setContent] = useState('');
  const [tags, setTags] = useState('');
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!content.trim()) return;

    setError(null);
    
    // Parse tags (comma-separated)
    const tagArray = tags
      .split(',')
      .map(tag => tag.trim().toLowerCase())
      .filter(tag => tag.length > 0);

    const postData: CreatePostRequest = {
      content: content.trim(),
      tags: tagArray,
    };

    try {
      if (onSubmit) {
        await onSubmit(postData);
        // Reset form on success
        setContent('');
        setTags('');
      }
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to create post';
      setError(errorMessage);
    }
  };

  return (
    <div className="card mb-8">
      <form onSubmit={handleSubmit}>
        {/* Error message */}
        {error && (
          <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg">
            <p className="text-red-600 text-sm">{error}</p>
          </div>
        )}

        {/* Content textarea */}
        <div className="mb-4">
          <label htmlFor="content" className="block text-sm font-medium text-gray-700 mb-2">
            Share your thoughts...
          </label>
          <textarea
            id="content"
            rows={4}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 resize-none"
            placeholder="What's on your mind about work, career, or professional life?"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            maxLength={2000}
            required
            disabled={isSubmitting}
          />
          <div className="flex justify-between items-center mt-1">
            <span className="text-xs text-gray-500">
              {content.length}/2000 characters
            </span>
          </div>
        </div>

        {/* Tags input */}
        <div className="mb-4">
          <label htmlFor="tags" className="block text-sm font-medium text-gray-700 mb-2">
            Tags (optional)
          </label>
          <input
            type="text"
            id="tags"
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            placeholder="burnout, interviews, promotion (comma-separated)"
            value={tags}
            onChange={(e) => setTags(e.target.value)}
            disabled={isSubmitting}
          />
        </div>

        {/* Submit button */}
        <div className="flex justify-end">
          <button
            type="submit"
            disabled={!content.trim() || isSubmitting}
            className="btn-primary disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
          >
            <PaperAirplaneIcon className="h-4 w-4" />
            <span>{isSubmitting ? 'Posting...' : 'Post'}</span>
          </button>
        </div>
      </form>
    </div>
  );
};

export default PostForm; 