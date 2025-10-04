
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_leetcode_stats(username,leetcode_Url = None):
    url = leetcode_Url if leetcode_Url else f"https://leetcode.com/{username}/"

    # url = f"https://leetcode.com/{username}/"
    
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0 Safari/537.36"
    )

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(3)  # wait for JS to load

    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()

    text = soup.get_text(" ", strip=True)

    rank_match = re.search(r"Rank\s*#?([\d,]+)", text, re.IGNORECASE)
    easy_match = re.search(r"Easy\s*(\d+)\s*/\s*(\d+)", text, re.IGNORECASE)
    med_match  = re.search(r"Med.\s*(\d+)\s*/\s*(\d+)", text, re.IGNORECASE)
    hard_match = re.search(r"Hard\s*(\d+)\s*/\s*(\d+)", text, re.IGNORECASE)

    recent_submission = None
    sub_link_tag = soup.find("a", href=lambda href: href and "/submissions/detail/" in href)
    if sub_link_tag:
        div = sub_link_tag.find("div", attrs={"data-title": True})
        if div:
            spans = div.find_all("span")
            problem_name = spans[0].get_text(strip=True) if len(spans) > 0 else None
            time_info = spans[1].get_text(strip=True) if len(spans) > 1 else None

            recent_submission = {
                "problem_name": problem_name,
                "time": time_info
            }
            
            easy = int(easy_match.group(1)) if easy_match else 0
            medium = int(med_match.group(1)) if med_match else 0
            hard = int(hard_match.group(1)) if hard_match else 0

    return {
        "rank": rank_match.group(1) if rank_match else None,
        "total_solved": easy+medium+hard,
        "easy": {
            "solved": easy,
            "total": int(easy_match.group(2)) if easy_match else None
        },
        "medium": {
            "solved": medium,
            "total": int(med_match.group(2)) if med_match else None
        },
        "hard": {
            "solved": hard,
            "total": int(hard_match.group(2)) if hard_match else None
        },
        "recent_submission": recent_submission
    }