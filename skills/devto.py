"""
DEV.to API Integration Module
https://developers.forem.com/api
"""

import os
import requests
from typing import Optional, Dict, List
from dotenv import load_dotenv

# Load .env file
load_dotenv()

API_KEY = os.getenv("DEVTO_API_KEY")
BASE_URL = "https://dev.to/api"

HEADERS = {
    "api-key": API_KEY,
    "Content-Type": "application/json"
}


def post_article(
    title: str,
    body_markdown: str,
    published: bool = False,
    tags: Optional[List[str]] = None,
    series: Optional[str] = None,
    canonical_url: Optional[str] = None
) -> Dict:
    """
    Create a new article on DEV.to
    
    Args:
        title: Article title
        body_markdown: Article content in markdown
        published: True to publish immediately, False for draft
        tags: List of tags (max 4)
        series: Series name for multi-part posts
        canonical_url: Original URL if cross-posting
    
    Returns:
        API response as dict
    """
    if not API_KEY:
        return {"error": "DEVTO_API_KEY not found in environment"}

    url = f"{BASE_URL}/articles"
    
    article_data = {
        "article": {
            "title": title,
            "body_markdown": body_markdown,
            "published": published
        }
    }
    
    if tags:
        article_data["article"]["tags"] = ",".join(tags[:4])
    if series:
        article_data["article"]["series"] = series
    if canonical_url:
        article_data["article"]["canonical_url"] = canonical_url
    
    try:
        response = requests.post(url, json=article_data, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def update_article(
    article_id: int,
    title: Optional[str] = None,
    body_markdown: Optional[str] = None,
    published: Optional[bool] = None,
    tags: Optional[List[str]] = None
) -> Dict:
    """
    Update an existing article
    """
    if not API_KEY:
        return {"error": "DEVTO_API_KEY not found in environment"}

    url = f"{BASE_URL}/articles/{article_id}"
    
    article_data = {"article": {}}
    
    if title:
        article_data["article"]["title"] = title
    if body_markdown:
        article_data["article"]["body_markdown"] = body_markdown
    if published is not None:
        article_data["article"]["published"] = published
    if tags:
        article_data["article"]["tags"] = ",".join(tags[:4])
    
    try:
        response = requests.put(url, json=article_data, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_article(article_id: int) -> Dict:
    """Get article by ID"""
    url = f"{BASE_URL}/articles/{article_id}"
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_my_articles() -> List[Dict]:
    """Get all my published articles"""
    if not API_KEY:
        return [{"error": "DEVTO_API_KEY not found in environment"}]

    url = f"{BASE_URL}/articles/me/published"
    try:
        response = requests.get(url, headers=HEADERS)
        return response.json()
    except requests.RequestException as e:
        return [{"error": str(e)}]
