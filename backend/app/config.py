import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings."""
    
    # MongoDB settings
    MONGODB_URI: str = os.getenv("MONGODB_URI", "")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "anti_linkedin")
    
    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Anti-LinkedIn API"
    
    # Security settings
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",  # Frontend dev
        "http://localhost:8000",  # Backend dev
        "https://your-frontend-domain.com"  # Production frontend
    ]
    
    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = 60
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
    
    # Content limits
    MAX_CONTENT_LENGTH: int = 2000
    MAX_TAGS_PER_POST: int = 10
    
    @classmethod
    def validate(cls):
        """Validate required settings."""
        if not cls.MONGODB_URI:
            raise ValueError("MONGODB_URI environment variable is required")

settings = Settings() 