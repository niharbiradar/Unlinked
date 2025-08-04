import motor.motor_asyncio
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017"
    database_name: str = "unlinked"
    
    class Config:
        env_file = ".env"

settings = Settings()

# Global database connection
client: Optional[motor.motor_asyncio.AsyncIOMotorClient] = None
database: Optional[motor.motor_asyncio.AsyncIOMotorDatabase] = None

async def init_db():
    """Initialize database connection"""
    global client, database
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
    database = client[settings.database_name]
    
    # Test the connection
    try:
        await client.admin.command('ping')
        print("✅ Connected to MongoDB")
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {e}")
        raise

async def close_db():
    """Close database connection"""
    global client
    if client:
        client.close()
        print("✅ Closed MongoDB connection")

def get_database() -> motor.motor_asyncio.AsyncIOMotorDatabase:
    """Get database instance"""
    if not database:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    return database

def get_collection(collection_name: str) -> motor.motor_asyncio.AsyncIOMotorCollection:
    """Get collection instance"""
    db = get_database()
    return db[collection_name] 