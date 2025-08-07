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
    <div className="card mb-8 animate-slide-up">
      <form onSubmit={handleSubmit}>
        {/* Error message */}
        {error && (
          <div className="mb-4 p-3 bg-gradient-to-r from-accent-600/20 to-accent-700/20 border border-accent-500/30 rounded-xl backdrop-blur-sm">
            <p className="text-accent-300 text-sm">{error}</p>
          </div>
        )}

        {/* Content textarea */}
        <div className="mb-4">
          <label htmlFor="content" className="block text-sm font-medium text-gray-200 mb-2">
            Share your thoughts...
          </label>
          <textarea
            id="content"
            rows={4}
            className="textarea-modern w-full"
            placeholder="What's on your mind about work, career, or professional life?"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            maxLength={2000}
            required
            disabled={isSubmitting}
          />
          <div className="flex justify-between items-center mt-1">
            <span className="text-xs text-gray-400">
              {content.length}/2000 characters
            </span>
          </div>
        </div>

        {/* Tags input */}
        <div className="mb-4">
          <label htmlFor="tags" className="block text-sm font-medium text-gray-200 mb-2">
            Tags (optional)
          </label>
          <input
            type="text"
            id="tags"
            className="input-modern w-full"
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