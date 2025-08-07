import requests
from bs4 import BeautifulSoup

def search(query):
    url = f"https://www.novelupdates.com/?s={query.replace(' ', '+')}&post_type=seriesplans"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    results = []
    for item in soup.select(".search_main_box_nu"):
        title_tag = item.select_one(".search_title > a")
        if title_tag:
            results.append({
                "title": title_tag.text.strip(),
                "url": title_tag["href"]
            })
    return results

def get_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.select_one("h1").text.strip()
    desc = soup.select_one("#editdescription").text.strip()
    return {
        "title": title,
        "description": desc,
        "url": url
    }
