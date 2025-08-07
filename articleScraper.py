# Scrape the article at https://www.npr.org/2024/11/13/nx-s1-5184493/spotify-ai-dj-music#:~:text=The%20New%20Yorker's%20Sanneh%20said,Chloee%20Weiner%20mixed%20the%20audio. with BeautifulSoup

from bs4 import BeautifulSoup
import requests

# URL of the article to scrape
url = "https://www.npr.org/2024/11/13/nx-s1-5184493/spotify-ai-dj-music"

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

# print(title)
# print(author)
# print(publication_date)
# print(content[:500])  # Print first 500 characters of content

import pandas as pd
# Create a DataFrame to store the scraped data
data = {
    "title": [title],
    "author": [author],
    "publication_date": [publication_date],
    "content": [content]
}
df = pd.DataFrame(data)
# Save the DataFrame to a CSV file
df.to_csv("npr_spotify_ai_dj_article.csv", index=False)