from dotenv import load_dotenv
load_dotenv()
import praw, os
import pandas as pd

# Setup Reddit API credentials (replace with your own)
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENTID"],
    client_secret=os.environ["REDDIT_SECRET"],
    user_agent='spotify_ai_dj_scraper'
)

# Search for posts about "Spotify AI DJ" in r/spotify
subreddit = reddit.subreddit("spotify")
posts = subreddit.search("AI DJ", limit=100)

data = []
for post in posts:
    data.append({
        "title": post.title,
        "score": post.score,
        "url": post.url,
        "num_comments": post.num_comments,
        "created_utc": post.created_utc,
        "selftext": post.selftext,
        "comments": [comment.body for comment in post.comments.list() if hasattr(comment, 'body')]
    })

# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv("reddit_spotify_ai_dj.csv", index=False)