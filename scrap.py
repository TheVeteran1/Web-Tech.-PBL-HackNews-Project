import requests
from bs4 import BeautifulSoup
import json
import os

def run_intel_scraper():
    print("[*] Initializing Scraper...")
    url = "https://thehackernews.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []
        
        posts = soup.find_all('div', class_='body-main')
        for post in posts[:15]:
            title = post.find('h2').text.strip()
            link = post.find('a')['href']
            # Automated Risk Tagging
            tag = "CRITICAL" if "exploit" in title.lower() or "zero-day" in title.lower() else "INTEL"
            
            articles.append({
                "title": title,
                "link": link,
                "source_id": "TheHackerNews",
                "tag": tag,
                "description": "Scraped real-time intelligence from primary sources."
            })
            
        with open('intel_data.json', 'w') as f:
            json.dump(articles, f, indent=4)
        print("[+] intel_data.json updated successfully.")
    except Exception as e:
        print(f"[-] Scrape Failed: {e}")

if __name__ == "__main__":
    run_intel_scraper()
