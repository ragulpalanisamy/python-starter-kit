"""MongoDB connection and client management using Motor async driver."""

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.utils.logger import get_logger

logger = get_logger(__name__)


class MongoDB:
    """MongoDB async client wrapper."""
    
    client: AsyncIOMotorClient | None = None
    database: AsyncIOMotorDatabase | None = None
    
    async def connect_db(self, mongodb_url: str, database_name: str) -> None:
        """
        Connect to MongoDB.
        
        Args:
            mongodb_url: MongoDB connection string
            database_name: Name of the database to use
        """
        try:
            self.client = AsyncIOMotorClient(mongodb_url)
            self.database = self.client[database_name]
            
            # Test connection
            await self.client.admin.command('ping')
            logger.info(f"Connected to MongoDB database: {database_name}")
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise
    
    async def close_db(self) -> None:
        """Close MongoDB connection."""
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed")
    
    def get_database(self) -> AsyncIOMotorDatabase:
        """
        Get the database instance.
        
        Returns:
            AsyncIOMotorDatabase instance
            
        Raises:
            RuntimeError: If database is not connected
        """
        if self.database is None:
            raise RuntimeError("Database not connected. Call connect_db() first.")
        return self.database
    
    def get_collection(self, collection_name: str):
        """
        Get a collection from the database.
        
        Args:
            collection_name: Name of the collection
            
        Returns:
            AsyncIOMotorCollection instance
        """
        db = self.get_database()
        return db[collection_name]


# Global MongoDB instance
mongodb = MongoDB()


async def get_mongodb() -> MongoDB:
    """
    Dependency to get MongoDB instance.
    
    Returns:
        MongoDB instance
    """
    return mongodb
