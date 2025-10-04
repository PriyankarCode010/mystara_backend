import requests
from bs4 import BeautifulSoup
import time

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
