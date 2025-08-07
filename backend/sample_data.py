#!/usr/bin/env python3
"""
Sample data script for Anti-LinkedIn MongoDB database.
This script adds sample posts and reactions for testing and development.
"""

import asyncio
import sys
import os
from datetime import datetime, timedelta, UTC
from bson import ObjectId

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

async def add_sample_data():
    """Add sample data to the database."""
    
    if not settings.MONGODB_URI:
        print("Error: MONGODB_URI not found in environment variables")
        return
    
    # Connect to MongoDB
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    db = client[settings.DATABASE_NAME]
    
    print(f"Adding sample data to database: {settings.DATABASE_NAME}")
    
    try:
        # Sample posts data
        sample_posts = [
            {
                "content": "Just had my third interview this week and I'm exhausted. Why do companies make you jump through so many hoops just to get a job?",
                "tags": ["interviews", "burnout", "jobsearch"],
                "is_private": False,
                "is_flagged": False,
                "created_at": datetime.now(UTC) - timedelta(hours=2),
                "reaction_counts": {"same": 12, "helpful": 8, "upvote": 15}
            },
            {
                "content": "Finally got promoted after 2 years! But now I'm terrified I'm not good enough for the new role. Anyone else feel like this?",
                "tags": ["promotion", "impostersyndrome", "career"],
                "is_private": False,
                "is_flagged": False,
                "created_at": datetime.now(UTC) - timedelta(hours=5),
                "reaction_counts": {"same": 25, "helpful": 18, "upvote": 32}
            },
            {
                "content": "My manager just told me to 'be more positive' when I raised concerns about workload. I'm already working 60+ hours a week. What am I supposed to do?",
                "tags": ["management", "workload", "burnout"],
                "is_private": False,
                "is_flagged": False,
                "created_at": datetime.now(UTC) - timedelta(hours=8),
                "reaction_counts": {"same": 45, "helpful": 22, "upvote": 67}
            },
            {
                "content": "Quit my toxic job today. Scared but relieved. Sometimes you just need to prioritize your mental health over a paycheck.",
                "tags": ["quitting", "mentalhealth", "career"],
                "is_private": False,
                "is_flagged": False,
                "created_at": datetime.now(UTC) - timedelta(hours=12),
                "reaction_counts": {"same": 89, "helpful": 56, "upvote": 123}
            },
            {
                "content": "Had a great conversation with my mentor today. Sometimes you just need someone to remind you that you're doing better than you think.",
                "tags": ["mentorship", "career", "growth"],
                "is_private": False,
                "is_flagged": False,
                "created_at": datetime.now(UTC) - timedelta(hours=15),
                "reaction_counts": {"same": 8, "helpful": 15, "upvote": 12}
            },
            {
                "content": "Why do job descriptions ask for 5+ years of experience for entry-level positions? How are we supposed to get experience if no one will hire us?",
                "tags": ["jobsearch", "entrylevel", "frustration"],
                "is_private": False,
                "is_flagged": False,
                "created_at": datetime.now(UTC) - timedelta(hours=18),
                "reaction_counts": {"same": 67, "helpful": 34, "upvote": 89}
            },
            {
                "content": "Today I realized I've been in the same role for 3 years with no growth opportunities. Time to start looking elsewhere.",
                "tags": ["career", "growth", "jobsearch"],
                "is_private": False,
                "is_flagged": False,
                "created_at": datetime.now(UTC) - timedelta(hours=24),
                "reaction_counts": {"same": 23, "helpful": 19, "upvote": 28}
            },
            {
                "content": "Just finished a major project that I've been working on for months. The feeling of accomplishment is incredible!",
                "tags": ["accomplishment", "projects", "career"],
                "is_private": False,
                "is_flagged": False,
                "created_at": datetime.now(UTC) - timedelta(hours=30),
                "reaction_counts": {"same": 5, "helpful": 12, "upvote": 18}
            }
        ]
        
        # Insert sample posts
        posts_collection = db.posts
        print("Adding sample posts...")
        
        inserted_posts = []
        for post in sample_posts:
            result = await posts_collection.insert_one(post)
            post["_id"] = result.inserted_id
            inserted_posts.append(post)
            print(f"✓ Added post: {post['content'][:50]}...")
        
        # Sample reactions data
        sample_reactions = []
        reaction_types = ["same", "helpful", "upvote"]
        
        # Add some reactions to the posts
        for post in inserted_posts[:4]:  # Add reactions to first 4 posts
            for reaction_type in reaction_types:
                # Add multiple reactions of each type
                for i in range(3):  # 3 reactions of each type per post
                    sample_reactions.append({
                        "post_id": post["_id"],
                        "reaction_type": reaction_type,
                        "created_at": datetime.now(UTC) - timedelta(minutes=i*10)
                    })
        
        # Insert sample reactions
        if sample_reactions:
            reactions_collection = db.reactions
            print("Adding sample reactions...")
            await reactions_collection.insert_many(sample_reactions)
            print(f"✓ Added {len(sample_reactions)} reactions")
        
        # Sample tags data
        sample_tags = [
            {"name": "burnout", "usage_count": 3},
            {"name": "interviews", "usage_count": 1},
            {"name": "jobsearch", "usage_count": 3},
            {"name": "promotion", "usage_count": 1},
            {"name": "impostersyndrome", "usage_count": 1},
            {"name": "career", "usage_count": 4},
            {"name": "management", "usage_count": 1},
            {"name": "workload", "usage_count": 1},
            {"name": "quitting", "usage_count": 1},
            {"name": "mentalhealth", "usage_count": 1},
            {"name": "mentorship", "usage_count": 1},
            {"name": "growth", "usage_count": 2},
            {"name": "entrylevel", "usage_count": 1},
            {"name": "frustration", "usage_count": 1},
            {"name": "accomplishment", "usage_count": 1},
            {"name": "projects", "usage_count": 1}
        ]
        
        # Insert sample tags
        tags_collection = db.tags
        print("Adding sample tags...")
        for tag in sample_tags:
            try:
                await tags_collection.insert_one(tag)
                print(f"✓ Added tag: {tag['name']}")
            except Exception as e:
                # Tag might already exist, that's okay
                print(f"Tag {tag['name']} already exists or error: {e}")
        
        print("\n🎉 Sample data added successfully!")
        print(f"\nAdded:")
        print(f"- {len(sample_posts)} sample posts")
        print(f"- {len(sample_reactions)} sample reactions")
        print(f"- {len(sample_tags)} sample tags")
        
    except Exception as e:
        print(f"Error adding sample data: {e}")
        import traceback
        traceback.print_exc()
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(add_sample_data()) 