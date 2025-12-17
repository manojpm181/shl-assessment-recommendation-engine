'''import requests
from bs4 import BeautifulSoup
import json
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE = "https://www.shl.com"
START_URLS = [
    "https://www.shl.com/solutions/products/product-catalog/",
    "https://www.shl.com/products/"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_session():
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session

def collect_links(session):
    links = set()

    for start in START_URLS:
        for page in range(1, 40):
            url = f"{start}?page={page}"
            print("Scanning:", url)

            try:
                r = session.get(url, headers=HEADERS, timeout=10, verify=False)
                if r.status_code != 200:
                    break
            except Exception as e:
                print("Page failed:", e)
                break

            soup = BeautifulSoup(r.text, "html.parser")
            page_count = 0

            for a in soup.find_all("a", href=True):
                href = a["href"]
                if "/products/" in href and "job-solutions" not in href:
                    if href.startswith("/"):
                        href = BASE + href
                    links.add(href)
                    page_count += 1

            if page_count == 0:
                break

            time.sleep(0.6)

    return list(links)

def scrape_product(session, url):
    r = session.get(url, headers=HEADERS, timeout=10, verify=False)
    soup = BeautifulSoup(r.text, "html.parser")

    title = soup.find("h1")
    title = title.text.strip() if title else "Unknown"

    desc = " ".join(p.text.strip() for p in soup.find_all("p"))

    return {
        "name": title,
        "url": url,
        "description": desc
    }

def main():
    session = get_session()

    links = collect_links(session)
    print("TOTAL LINKS FOUND:", len(links))

    results = []
    for i, link in enumerate(links):
        try:
            data = scrape_product(session, link)
            results.append(data)
            print(f"[{i+1}/{len(links)}] {data['name']}")
            time.sleep(0.5)
        except Exception as e:
            print("Failed:", link, e)

    with open("data/raw_assessments.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("Saved data/raw_assessments.json")

if __name__ == "__main__":
    main()
'''
import requests
from bs4 import BeautifulSoup
import json
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE = "https://www.shl.com"
START_URLS = [
    "https://www.shl.com/solutions/products/product-catalog/",
    "https://www.shl.com/products/"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_session():
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session

def collect_links(session):
    links = set()

    for start in START_URLS:
        page = 1
        while True:
            url = f"{start}?page={page}"
            print("Scanning:", url)

            try:
                r = session.get(url, headers=HEADERS, timeout=10, verify=False)
                if r.status_code != 200:
                    print(f"Page {page} failed with status {r.status_code}")
                    break
            except Exception as e:
                print("Request failed:", e)
                break

            soup = BeautifulSoup(r.text, "html.parser")
            new_links_count = 0

            for a in soup.find_all("a", href=True):
                href = a["href"].strip()
                # Broader matching: any link containing 'product' but not job-solutions
                if "product" in href.lower() and "job-solutions" not in href.lower():
                    if href.startswith("/"):
                        href = BASE + href
                    if href not in links:
                        links.add(href)
                        new_links_count += 1

            print(f"Found {new_links_count} new links on page {page}")

            if new_links_count == 0:
                print("No new links, moving to next start URL.")
                break

            page += 1
            time.sleep(0.5)  # polite delay

    return list(links)

def scrape_product(session, url):
    try:
        r = session.get(url, headers=HEADERS, timeout=10, verify=False)
        if r.status_code != 200:
            return None

        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.find("h1")
        title = title.text.strip() if title else "Unknown"
        desc = " ".join(p.text.strip() for p in soup.find_all("p"))

        return {
            "name": title,
            "url": url,
            "description": desc
        }
    except Exception as e:
        print("Scrape failed:", url, e)
        return None

def main():
    session = get_session()

    links = collect_links(session)
    print("TOTAL LINKS FOUND:", len(links))

    results = []
    for i, link in enumerate(links):
        data = scrape_product(session, link)
        if data:
            results.append(data)
            print(f"[{i+1}/{len(links)}] {data['name']}")
        time.sleep(0.3)

    with open("data/raw_assessments.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("Saved data/raw_assessments.json")

if __name__ == "__main__":
    main()

