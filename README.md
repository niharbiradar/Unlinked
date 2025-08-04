# Unlinked - Professional Networking Platform

A modern, privacy-focused professional networking platform built as an alternative to LinkedIn.

## 🚀 Tech Stack

### Frontend
- **Next.js 13** with App Router and TypeScript
- **Tailwind CSS** for styling with dark/light mode support
- **React Query** for server state management
- **Axios** for HTTP requests

### Backend
- **FastAPI** for high-performance async Python API
- **Motor** async MongoDB driver
- **Pydantic** for data validation
- **Python 3.11+**

### Infrastructure
- **Docker** for containerization
- **MongoDB** for document database
- **Docker Compose** for local development

## 📁 Project Structure

```
Unlinked/
├── frontend/                 # Next.js frontend application
│   ├── app/                 # Next.js App Router pages
│   ├── components/          # Reusable React components
│   ├── styles/              # Global styles and Tailwind config
│   ├── package.json         # Frontend dependencies
│   └── Dockerfile           # Frontend container
├── backend/                 # FastAPI backend application
│   ├── main.py             # FastAPI application entry point
│   ├── routers/            # API route modules
│   ├── models/             # Data models and schemas
│   ├── db/                 # Database connection utilities
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Backend container
├── docker-compose.yml      # Local development setup
├── PROJECT_LOG.md          # Development progress and decisions
└── README.md               # This file
```

## 🛠️ Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### Option 1: Docker Compose (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Unlinked
   ```

2. **Start all services**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Option 2: Local Development

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

#### Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### MongoDB Setup
```bash
# Install MongoDB locally or use Docker
docker run -d -p 27017:27017 --name mongodb mongo:7.0
```

## 🔧 Development

### Frontend Development
- **Development server**: `npm run dev`
- **Build**: `npm run build`
- **Type checking**: `npm run type-check`
- **Linting**: `npm run lint`

### Backend Development
- **Development server**: `uvicorn main:app --reload`
- **API documentation**: Available at `/docs` (Swagger UI)
- **Health check**: `GET /api/health`

### Database
- **Connection**: MongoDB with Motor async driver
- **Default URL**: `mongodb://localhost:27017/unlinked`
- **Collections**: Will be created automatically as needed

## 🧪 Testing

### Frontend Testing
```bash
cd frontend
npm test
```

### Backend Testing
```bash
cd backend
pytest
```

## 🐳 Docker Commands

### Build Images
```bash
# Build all services
docker-compose build

# Build specific service
docker-compose build frontend
docker-compose build backend
```

### Development
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild and restart
docker-compose up -d --build
```

### Production
```bash
# Build production images
docker build -f frontend/Dockerfile ./frontend --target production
docker build -f backend/Dockerfile ./backend --target production
```

## 📋 API Endpoints

### Health Check
- `GET /api/health` - Check API and database health

### Authentication (Planned)
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### Users (Planned)
- `GET /api/users/me` - Get current user profile
- `PUT /api/users/me` - Update user profile
- `GET /api/users/{id}` - Get user by ID

### Posts (Planned)
- `GET /api/posts` - Get feed posts
- `POST /api/posts` - Create new post
- `GET /api/posts/{id}` - Get specific post

## 🔒 Environment Variables

### Backend (.env)
```env
MONGODB_URL=mongodb://localhost:27017/unlinked
DATABASE_NAME=unlinked
SECRET_KEY=your-secret-key
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🎨 Features

### Current Features
- ✅ Modern Next.js 13 frontend with TypeScript
- ✅ Tailwind CSS with dark/light mode support
- ✅ FastAPI backend with async MongoDB
- ✅ Docker containerization
- ✅ Health check endpoint
- ✅ CORS configuration
- ✅ Responsive design

### Planned Features
- 🔄 User authentication and authorization
- 🔄 Profile management
- 🔄 Post creation and feed
- 🔄 Connection/following system
- 🔄 Search functionality
- 🔄 Real-time messaging
- 🔄 Content moderation
- 🔄 Analytics dashboard

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Check the [PROJECT_LOG.md](PROJECT_LOG.md) for development decisions
- Review the API documentation at http://localhost:8000/docs
- Open an issue on GitHub

---

**Built with ❤️ for better professional networking**
