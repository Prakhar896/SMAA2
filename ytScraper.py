from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd

# Replace with your target video URL or ID
video_urls = [
    "https://www.youtube.com/shorts/grUJ97ajA4Y",
    "https://www.youtube.com/watch?v=iFAWLhcBNaA",
    "https://www.youtube.com/watch?v=0ZF35dPoBeE",
    "https://www.youtube.com/watch?v=ok-aNnc0Dko",
    "https://www.youtube.com/watch?v=ozF85QOz6Dg"
]

downloader = YoutubeCommentDownloader()
comments = []

# Fetch first 100 comments for each video
for url in video_urls:
    vidCommentCount = 0
    vidComments = downloader.get_comments_from_url(url, sort_by=0)
    for comment in vidComments:
        comments.append({
            "author": comment["author"],
            "text": comment["text"],
            "time": comment["time"],
            "votes": comment["votes"],
        })
        vidCommentCount += 1
        
        if vidCommentCount >= 100:  # limit to 100 comments per video
            break
    print("Fetched {} comments from {}".format(vidCommentCount, url))

# Save to CSV
df = pd.DataFrame(comments)
df.to_csv("youtube_spotify_ai_dj_comments.csv", index=False)

print("Saved {} comments to youtube_spotify_ai_dj_comments.csv".format(len(comments)))