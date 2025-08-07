# Anti-LinkedIn Frontend

A React-based frontend for Anti-LinkedIn, a minimalist, anonymous social platform for career-related thoughts and reflections.

## Features

- 📱 **Mobile-friendly design** - Responsive layout that works on all devices
- 🎨 **Modern UI** - Clean, minimalist design with Tailwind CSS
- 📝 **Anonymous posting** - Share thoughts without profiles or personal info
- 🏷️ **Tag system** - Organize posts with relevant tags
- 💬 **Simple reactions** - React with "same", "helpful", and "upvote"
- ⚡ **Fast performance** - Optimized with React and TypeScript

## Tech Stack

- **React 18** - Modern React with hooks
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first CSS framework
- **Heroicons** - Beautiful SVG icons
- **Headless UI** - Accessible UI components

## Project Structure

```
frontend/
├── public/                 # Static assets
├── src/
│   ├── components/         # Reusable components
│   │   ├── Layout/        # Layout components
│   │   │   ├── Header.tsx
│   │   │   └── Layout.tsx
│   │   ├── Post/          # Post-related components
│   │   │   ├── PostCard.tsx
│   │   │   └── PostForm.tsx
│   │   └── Feed/          # Feed components
│   │       └── Feed.tsx
│   ├── App.tsx            # Main application component
│   ├── index.tsx          # Application entry point
│   └── index.css          # Global styles and Tailwind
├── package.json           # Dependencies and scripts
├── tailwind.config.js     # Tailwind CSS configuration
└── tsconfig.json          # TypeScript configuration
```

## Getting Started

### Prerequisites

- Node.js 16+ 
- npm or yarn

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm start
   ```

3. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

### Available Scripts

- `npm start` - Start development server
- `npm run build` - Build for production
- `npm test` - Run tests
- `npm run eject` - Eject from Create React App

## Development

### Component Structure

The application follows a modular component structure:

- **Layout Components** - Handle overall page structure and navigation
- **Post Components** - Handle individual posts and post creation
- **Feed Components** - Handle the feed display and post listing

### Styling

The app uses Tailwind CSS for styling with custom components defined in `src/index.css`:

- `.btn-primary` - Primary button styling
- `.btn-secondary` - Secondary button styling  
- `.card` - Card container styling

### State Management

Currently using React's built-in state management with `useState`. For larger applications, consider adding:

- React Query for server state
- Zustand or Redux for client state
- React Context for theme/auth state

## Design Principles

- **Mobile-first** - All components designed for mobile first
- **Accessibility** - WCAG compliant components
- **Performance** - Optimized for fast loading
- **Simplicity** - Clean, uncluttered interface

## Future Enhancements

- [ ] Backend integration
- [ ] Real-time updates
- [ ] Dark mode
- [ ] Offline support
- [ ] Push notifications
- [ ] Advanced filtering
- [ ] User preferences

## Contributing

1. Follow the existing code structure
2. Use TypeScript for all new components
3. Add proper TypeScript interfaces
4. Follow the established naming conventions
5. Test on mobile devices

## License

This project is part of the Anti-LinkedIn platform.
