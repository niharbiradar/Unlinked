What is Anti-LinkedIn?
Anti-LinkedIn is a minimalist, anonymous social platform designed to provide a safe, low-pressure space for people to share their real, unfiltered thoughts and feelings about their careers — without the performative culture, clout-chasing, and toxicity commonly found on LinkedIn.
It’s a digital "vent wall" for career-related frustrations, doubts, wins, and reflections, built to help users feel seen and less alone, with no profiles, no follower counts, and no personal branding.

Why Anti-LinkedIn?
LinkedIn often creates burnout and comparison fatigue by encouraging users to showcase only their successes and professional highlights. Many users feel trapped in a cycle of constant self-promotion and perfection, which can be mentally exhausting and isolating.
Anti-LinkedIn breaks that pattern by allowing:

Anonymous posting: No names, no job titles, no resumes.
Emotion-first expression: Sharing how work really feels.
No networking pressure: No comments, no clout metrics — just simple reactions.
Chronological, algorithm-free feed: Just real, raw posts from people like you.
Optional private journaling: A space to reflect without publishing.
Core Features (MVP)
Anonymous posts with career-related thoughts and reflections.
Simple reaction system: “Same,” “Helpful,” and “Upvote” — no likes or follower metrics.
Tagging system for themes like #burnout, #impostersyndrome, #interviews.
Content flagging for moderation.
Responsive, mobile-friendly frontend.
Secure, performant backend using FastAPI and MongoDB.
Tech Stack
Frontend: Next.js 13 with TypeScript, React Query, Tailwind CSS
Backend: FastAPI with Motor (async MongoDB driver)
Database: MongoDB Atlas
Infrastructure: Docker for consistent dev and deployment environments
Development Notes
The app prioritizes security, scalability, and maintainability.
Input validation and sanitization are enforced on all backend endpoints.
MongoDB indexes optimize feed loading and tag filtering.
The app follows best practices to prevent NoSQL injection and XSS attacks.
All code is modular, well-documented, and follows established style guides.
Next Steps
Build API routes for posts, reactions, and flagging.
Develop frontend components for feed display and post creation.
Implement moderation workflows.
Add optional minimal authentication (future).
