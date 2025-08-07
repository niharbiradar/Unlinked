#!/usr/bin/env python3
"""
Schema setup script for Anti-LinkedIn MongoDB database.
This script creates the necessary collections and indexes for the anonymous social platform.
"""

import asyncio
import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING, DESCENDING
from app.config import settings

async def setup_schema():
    """Set up MongoDB collections and indexes for Anti-LinkedIn."""
    
    if not settings.MONGODB_URI:
        print("Error: MONGODB_URI not found in environment variables")
        return
    
    # Connect to MongoDB
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    db = client[settings.DATABASE_NAME]
    
    print(f"Setting up schema for database: {settings.DATABASE_NAME}")
    
    try:
        # 1. Posts Collection
        print("Creating posts collection...")
        posts_collection = db.posts
        
        # Create indexes for posts
        await posts_collection.create_index([("created_at", DESCENDING)])  # For chronological feed
        await posts_collection.create_index([("tags", ASCENDING)])  # For tag filtering
        await posts_collection.create_index([("is_flagged", ASCENDING)])  # For moderation
        await posts_collection.create_index([("is_private", ASCENDING)])  # For private journaling
        
        print("✓ Posts collection and indexes created")
        
        # 2. Reactions Collection
        print("Creating reactions collection...")
        reactions_collection = db.reactions
        
        # Create indexes for reactions
        await reactions_collection.create_index([("post_id", ASCENDING)])
        await reactions_collection.create_index([("reaction_type", ASCENDING)])  # "same", "helpful", "upvote"
        await reactions_collection.create_index([("post_id", ASCENDING), ("reaction_type", ASCENDING)])  # Compound index
        
        print("✓ Reactions collection and indexes created")
        
        # 3. Flags Collection (for moderation)
        print("Creating flags collection...")
        flags_collection = db.flags
        
        # Create indexes for flags
        await flags_collection.create_index([("post_id", ASCENDING)])
        await flags_collection.create_index([("created_at", DESCENDING)])
        await flags_collection.create_index([("status", ASCENDING)])  # "pending", "reviewed", "resolved"
        
        print("✓ Flags collection and indexes created")
        
        # 4. Tags Collection (for tag management and analytics)
        print("Creating tags collection...")
        tags_collection = db.tags
        
        # Create indexes for tags
        await tags_collection.create_index([("name", ASCENDING)], unique=True)
        await tags_collection.create_index([("usage_count", DESCENDING)])
        
        print("✓ Tags collection and indexes created")
        
        print("\n🎉 Schema setup completed successfully!")
        print("\nCollections created:")
        print("- posts: Anonymous career-related posts")
        print("- reactions: Simple reactions (same, helpful, upvote)")
        print("- flags: Content moderation flags")
        print("- tags: Tag management and analytics")
        
        print("\nKey indexes created:")
        print("- Chronological feed ordering (created_at)")
        print("- Tag filtering and search")
        print("- Moderation workflow support")
        print("- Reaction aggregation")
        
    except Exception as e:
        print(f"Error setting up schema: {e}")
        import traceback
        traceback.print_exc()
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(setup_schema()) 