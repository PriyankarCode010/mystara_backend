import requests
from bs4 import BeautifulSoup
import sys
import json

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

def scrape_gfg_profile(username):
    url = f"https://www.geeksforgeeks.org/user/{username}"
    headers = {"User-Agent": USER_AGENT}

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    data = {}

    name_tag = soup.find("div",class_="profilePicSection_head_userHandle__oOfFy")
    institute_tag = soup.find("div", class_="educationDetails_head_left--text__tgi9I")

    data["name"] = name_tag.get_text(strip=True) if name_tag else None
    data["institute"] = institute_tag.get_text(strip=True) if institute_tag else None

    score_tag = soup.find("div", class_="scoreCard_head_left--score__oSi_x")
    data["coding_score"] = score_tag.get_text(strip=True) if score_tag else None

    rank_tag = soup.find("span", class_="educationDetails_head_left_userRankContainer--text__wt81s")
    data["rank"] = rank_tag.get_text(strip=True) if rank_tag else None

    total_solved = soup.find("div", class_="scoreCard_head_left--score__oSi_x")
    data["total_solved"] = total_solved.get_text(strip=True) if rank_tag else None

    return data

# Command line interface for Node.js
if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print(json.dumps({"error": "Username is required"}))
            sys.exit(1)
        
        username = sys.argv[1]
        
        result = scrape_gfg_profile(username)
        print(json.dumps(result))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)