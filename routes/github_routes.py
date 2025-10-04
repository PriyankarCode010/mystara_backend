from fastapi import APIRouter
from utils.github_scraper import scrape_github_user

router = APIRouter(prefix="/github", tags=["GitHub"])

@router.get("/{username}")
def get_github_data(username: str, url: str = None):
    return scrape_github_user(username, url)
