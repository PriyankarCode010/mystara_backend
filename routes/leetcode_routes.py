from fastapi import APIRouter
from utils.leetcode_scraper import scrape_leetcode_stats

router = APIRouter(prefix="/leetcode", tags=["LeetCode"])

@router.get("/{username}")
def get_leetcode_data(username: str, url: str = None):
    return scrape_leetcode_stats(username,url)
