from bs4 import BeautifulSoup
import requests, json, time, os, sys

# URL of the article to scrape
url = "https://mixmag.asia/read/spotify-launches-new-ai-feature-dj-radio-commentary-tech/"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the title
    title = soup.find('h1').get_text(strip=True)
    
    # Extract the article content
    paragraphs = soup.find_all('p')
    content = ' '.join([para.get_text(strip=True) for para in paragraphs])
    
    # Extract the author if available
    author_tag = soup.find('p', class_='byline__name')
    author = author_tag.get_text(strip=True) if author_tag else "Unknown"
    
    # Extract the publication date
    date_tag = soup.find('time')
    publication_date = date_tag['datetime'] if date_tag else "Unknown"
    
    # Print the extracted information
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Publication Date: {publication_date}")
    print(f"Content: {content[:500]}...")  # Print first 500 characters of content
else:
    print(f"Failed to retrieve the article. Status code: {response.status_code}")
    sys.exit(1)

# print(title)
# print(author)
# print(publication_date)
# print(content[:500])  # Print first 500 characters of content

root = 'articles'
filename = os.path.join(root, 'Mixmag.json')

quoteCleaner = lambda text: text.replace('\u2018', "'").replace('\u2019', "'").replace("\u201c", '"').replace("\u201d", '"')

title = title.encode('utf-8').decode('ascii', 'ignore')
author = author.encode('utf-8').decode('ascii', 'ignore')
content = content.encode('utf-8').decode('ascii', 'ignore')


# title = quoteCleaner(title)
# author = quoteCleaner(author)
# content = quoteCleaner(content)

data = {
    "url": url,
    "title": title,
    "author": author,
    "publication_date": publication_date,
    "content": content
}

json.dump(data, open(filename, 'w'), indent=4)