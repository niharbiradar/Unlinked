from fastapi import APIRouter, HTTPException
from db.database import get_database

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint to verify API and database connectivity
    """
    try:
        # Test database connection
        db = get_database()
        await db.command("ping")
        
        return {
            "status": "ok",
            "message": "API and database are healthy",
            "timestamp": "2024-01-01T00:00:00Z"
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Service unhealthy: {str(e)}"
        ) 