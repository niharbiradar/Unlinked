from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import logging

from .config import settings
from .database import database
from .api.v1.api import api_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Validate settings
settings.validate()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Security middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "your-domain.com"]  # Update for production
)

# Set up CORS with more restrictive settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
    max_age=3600,  # Cache preflight requests for 1 hour
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.on_event("startup")
async def startup_event():
    """Startup event - connect to database."""
    try:
        await database.connect()
        logger.info("Application startup completed")
    except Exception as e:
        logger.error(f"Failed to start application: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event - disconnect from database."""
    await database.disconnect()
    logger.info("Application shutdown completed")

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Anti-LinkedIn API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    try:
        db_healthy = await database.health_check()
        if not db_healthy:
            raise HTTPException(status_code=503, detail="Database connection failed")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail="Service unhealthy") 