import { ThemeToggle } from '@/components/theme-toggle';
import { Header } from '@/components/header';

export default function Home() {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="text-center">
          <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-6xl">
            Welcome to{' '}
            <span className="text-primary">Unlinked</span>
          </h1>
          <p className="mt-6 text-lg leading-8 text-muted-foreground">
            A professional networking platform that puts you first.
            Connect, share, and grow without the noise.
          </p>
          <div className="mt-10 flex items-center justify-center gap-x-6">
            <button className="btn-primary px-6 py-3 text-base">
              Get Started
            </button>
            <button className="btn-outline px-6 py-3 text-base">
              Learn More
            </button>
          </div>
        </div>
        
        <div className="mt-16 grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
          <div className="rounded-lg border bg-card p-6">
            <h3 className="text-lg font-semibold text-card-foreground">
              Professional Profiles
            </h3>
            <p className="mt-2 text-sm text-muted-foreground">
              Create a profile that showcases your skills and experience without the clutter.
            </p>
          </div>
          
          <div className="rounded-lg border bg-card p-6">
            <h3 className="text-lg font-semibold text-card-foreground">
              Meaningful Connections
            </h3>
            <p className="mt-2 text-sm text-muted-foreground">
              Connect with professionals who share your interests and goals.
            </p>
          </div>
          
          <div className="rounded-lg border bg-card p-6">
            <h3 className="text-lg font-semibold text-card-foreground">
              Quality Content
            </h3>
            <p className="mt-2 text-sm text-muted-foreground">
              Share insights and engage with content that matters to your career.
            </p>
          </div>
        </div>
      </main>
    </div>
  );
} 