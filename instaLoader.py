import instaloader

# Create an instance
L = instaloader.Instaloader()

# Load a public hashtag page (e.g., #SpotifyAIDJ)
hashtag = 'aidj'
posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()

data = []
for post in posts:
    data.append({
        "title": post.title,
        "caption": post.caption,
        "likes": post.likes,
        "commentCount": post.comments,
        "comments": [comment.text for comment in post.get_comments()],
        "date_utc": post.date_utc.isoformat(),
        "url": post.shortcode
    })
    if len(data) >= 200:  # limit to 200 posts
        break

import pandas as pd
df = pd.DataFrame(data)
df.to_csv("instagram_spotify_ai_dj.csv", index=False)