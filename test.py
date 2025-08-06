# Scrape instagram for posts on "Spotify Wrapped"

import requests
from bs4 import BeautifulSoup
def scrape_instagram_posts(tag):
    url = f"https://www.instagram.com/explore/tags/{tag}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = []
    
    for post in soup.find_all('article'):
        for link in post.find_all('a'):
            href = link.get('href')
            if href and '/p/' in href:
                posts.append(f"https://www.instagram.com{href}")
    
    return posts

if __name__ == "__main__":
    tag = "spotify"
    posts = scrape_instagram_posts(tag)
    print(posts)
    
    if posts:
        print(f"Found {len(posts)} posts for #{tag}:")
        for post in posts:
            print(post)
    else:
        print(f"No posts found for #{tag}.")