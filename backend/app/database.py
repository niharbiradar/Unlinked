from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings
import logging

logger = logging.getLogger(__name__)

class Database:
    """Database connection manager."""
    
    def __init__(self):
        self.client: AsyncIOMotorClient = None
        self.database = None
    
    async def connect(self):
        """Connect to MongoDB with connection pooling."""
        try:
            # Configure connection pooling for better performance
            self.client = AsyncIOMotorClient(
                settings.MONGODB_URI,
                maxPoolSize=10,  # Maximum number of connections in the pool
                minPoolSize=1,   # Minimum number of connections in the pool
                maxIdleTimeMS=30000,  # Close connections after 30 seconds of inactivity
                serverSelectionTimeoutMS=5000,  # 5 second timeout for server selection
                connectTimeoutMS=10000,  # 10 second timeout for connection
                socketTimeoutMS=5000,  # 5 second timeout for socket operations
            )
            self.database = self.client[settings.DATABASE_NAME]
            
            # Test the connection
            await self.client.admin.command('ping')
            logger.info(f"Connected to MongoDB database: {settings.DATABASE_NAME}")
            
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise
    
    async def disconnect(self):
        """Disconnect from MongoDB."""
        if self.client:
            self.client.close()
            logger.info("Disconnected from MongoDB")
    
    def get_collection(self, collection_name: str):
        """Get a collection from the database."""
        if self.database is None:
            raise RuntimeError("Database not connected. Call connect() first.")
        return self.database[collection_name]
    
    async def health_check(self) -> bool:
        """Check if database connection is healthy."""
        try:
            if self.client is None:
                return False
            await self.client.admin.command('ping')
            return True
        except Exception:
            return False

# Global database instance
database = Database() 