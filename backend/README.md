# Anti-LinkedIn Backend

FastAPI backend for Anti-LinkedIn with MongoDB integration.

## Project Structure

```
backend/
├── app/                    # Main application package
│   ├── __init__.py
│   ├── main.py            # FastAPI application
│   ├── config.py          # Configuration and settings
│   ├── database.py        # Database connection and utilities
│   ├── api/               # API routes
│   │   └── v1/           # API version 1
│   │       ├── __init__.py
│   │       ├── api.py    # Main API router
│   │       └── endpoints/ # API endpoints
│   │           ├── __init__.py
│   │           └── posts.py
│   └── models/           # Pydantic models
│       ├── __init__.py
│       ├── post.py
│       └── reaction.py
├── main.py               # Application entry point
├── schema_setup.py      # Database schema setup script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the backend directory:
```bash
cp env.example .env
```

4. Update the `.env` file with your MongoDB URI and database name.

5. Set up the database schema:
```bash
python schema_setup.py
```

6. Run the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`
API documentation will be available at `http://localhost:8000/docs`

## API Endpoints

### Posts
- `POST /api/v1/posts/` - Create a new anonymous post
- `GET /api/v1/posts/` - Get posts (chronological order)
- `GET /api/v1/posts/{post_id}` - Get a specific post

## Database Schema

The schema includes the following collections:

- **posts**: Anonymous career-related posts with tags and privacy settings
- **reactions**: Simple reactions (same, helpful, upvote) for posts
- **flags**: Content moderation flags for inappropriate content
- **tags**: Tag management and usage analytics

All collections include appropriate indexes for optimal performance.

## Development

The backend follows FastAPI best practices with:
- Modular structure with clear separation of concerns
- Pydantic models for data validation
- Async/await for database operations
- Proper error handling and HTTP status codes
- CORS middleware for frontend integration 