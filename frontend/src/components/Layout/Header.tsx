import React from 'react';
import { Bars3Icon } from '@heroicons/react/24/outline';

interface HeaderProps {
  onMenuClick?: () => void;
}

const Header: React.FC<HeaderProps> = ({ onMenuClick }) => {
  return (
    <header className="bg-gradient-to-r from-black-950/90 to-black-900/90 backdrop-blur-md border-b border-dark-700/50 sticky top-0 z-50 shadow-dark-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo/Brand */}
          <div className="flex items-center">
            <h1 className="text-xl font-bold gradient-text">
              Anti-LinkedIn
            </h1>
          </div>

          {/* Mobile menu button */}
          <div className="flex items-center sm:hidden">
            <button
              type="button"
              className="inline-flex items-center justify-center p-2 rounded-xl text-gray-400 hover:text-blue-400 hover:bg-dark-700/50 focus:outline-none focus:ring-2 focus:ring-blue-500/50 transition-all duration-200"
              onClick={onMenuClick}
            >
              <span className="sr-only">Open main menu</span>
              <Bars3Icon className="block h-6 w-6" aria-hidden="true" />
            </button>
          </div>

          {/* Desktop navigation */}
          <nav className="hidden sm:flex space-x-8">
            <button className="text-gray-400 hover:text-blue-400 px-3 py-2 rounded-xl text-sm font-medium transition-all duration-200 hover:bg-dark-700/50">
              Feed
            </button>
            <button className="text-gray-400 hover:text-blue-400 px-3 py-2 rounded-xl text-sm font-medium transition-all duration-200 hover:bg-dark-700/50">
              Post
            </button>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header; 