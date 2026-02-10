"""
DEV.to API Skill
Post articles to DEV.to community using API
"""

import os
import requests
from typing import Optional, Dict

DEVTO_API_KEY = os.getenv("DEVTO_API_KEY")
DEVTO_API_URL = "https://dev.to/api/articles"

def post_article(title: str, body_markdown: str, published: bool = False, 
                 tags: list = None, series: str = None) -> Optional[Dict]:
    """
    Post an article to DEV.to
    
    Args:
        title: Article title
        body_markdown: Article content in markdown
        published: True to publish immediately, False for draft
        tags: List of tags (max 4)
        series: Series name if part of a series
    
    Returns:
        Response JSON or None if failed
    """
    if not DEVTO_API_KEY:
        return {"error": "DEV.to API key not found in DEVTO_API_KEY env var"}
    
    headers = {
        "api-key": DEVTO_API_KEY,
        "Content-Type": "application/json"
    }
    
    art