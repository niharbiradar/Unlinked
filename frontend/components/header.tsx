'use client';

import { ThemeToggle } from './theme-toggle';

export function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between px-4">
        <div className="flex items-center space-x-4">
          <h1 className="text-xl font-bold text-foreground">
            Unlinked
          </h1>
          <nav className="hidden md:flex items-center space-x-6">
            <a
              href="#"
              className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
            >
              Home
            </a>
            <a
              href="#"
              className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
            >
              Network
            </a>
            <a
              href="#"
              className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
            >
              Jobs
            </a>
            <a
              href="#"
              className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
            >
              Messages
            </a>
          </nav>
        </div>
        
        <div className="flex items-center space-x-4">
          <button className="btn-outline px-4 py-2 text-sm">
            Sign In
          </button>
          <button className="btn-primary px-4 py-2 text-sm">
            Sign Up
          </button>
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
} 