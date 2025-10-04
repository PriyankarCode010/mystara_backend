import requests
from bs4 import BeautifulSoup
import time
import sys
import json

USER_AGENT = "MyScraperBot/1.0"

def scrape_github_user(username, github_Url = None):
    url = github_Url if github_Url else f"https://github.com/{username}?tab=repositories"
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    repos = []
    for repo_tag in soup.select("a[itemprop='name codeRepository']"):
        repos.append(repo_tag.get_text(strip=True))
    return {
        "repos":repos,
        "total_repos":len(repos)
    }

# Command line interface for Node.js
if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print(json.dumps({"error": "Username is required"}))
            sys.exit(1)
        
        username = sys.argv[1]
        url = sys.argv[2] if len(sys.argv) > 2 else None
        
        result = scrape_github_user(username, url)
        print(json.dumps(result))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
