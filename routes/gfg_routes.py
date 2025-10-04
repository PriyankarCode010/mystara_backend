from fastapi import APIRouter
from utils.gfg_scraper import scrape_gfg_profile

router = APIRouter(prefix="/gfg", tags=["GeeksForGeeks"])

@router.get("/{username}")
def get_gfg_data(username: str):
    return scrape_gfg_profile(username)
