import os
from googleapiclient.discovery import build
from typing import Dict, Any
import googleapiclient.discovery
import matplotlib.pyplot as plt
from collections import defaultdict

def get_channel_id_from_username(yt, username: str) -> str:
    """
    Converts a YouTube username to a channel ID.
    """
    request = yt.channels().list(
        part="id",
        forUsername=username
    )
    response = request.execute()
    items = response.get("items", [])
    if items:
        return items[0]["id"]
    else:
        raise ValueError(f"No channel found for username: {username}")

def get_all_videos(yt, channel_id: str):
    """
    Retrieves all video IDs for a channel.
    """
    videos = []
    request = yt.search().list(
        part="id",
        channelId=channel_id,
        maxResults=50,
        order="date",
        type="video"
    )
    while request:
        response = request.execute()
        for item in response.get("items", []):
            videos.append(item["id"]["videoId"])
        request = yt.search().list_next(request, response)
    return videos

def get_video_details(yt, video_ids):
    """
    Retrieves video details (publishedAt, viewCount) for a list of video IDs.
    """
    details = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        request = yt.videos().list(
            part="snippet,statistics",
            id=",".join(batch)
        )
        response = request.execute()
        for item in response.get("items", []):
            published = item["snippet"]["publishedAt"]
            views = int(item["statistics"].get("viewCount", 0))
            details.append((published[:4], views))
    return details

def channel_view_count_by_year(yt, channel_id: str) -> None:
    """
    Aggregates and plots view counts by year for all videos in a channel.
    """
    video_ids = get_all_videos(yt, channel_id)
    video_details = get_video_details(yt, video_ids)
    view_counts = defaultdict(int)
    for year, views in video_details:
        view_counts[year] += views
    years = sorted(view_counts.keys())
    view_counts_list = [view_counts[year] for year in years]
    plt.bar(years, view_counts_list)
    plt.xlabel("Year")
    plt.ylabel("View Count")
    plt.title(f"Channel View Count by Year for {channel_id}")
    plt.xticks(years)
    plt.show()

def main():
    api_key = os.environ["youtube_api_key"]
    yt = build("youtube", "v3", developerKey=api_key)
    # Replace with actual channel ID or username
    username = "MrBeast"  # e.g., "MrBeast"
    channel_id = "UCX6OQ3DkcsbYNE6H8uQQuVA"  # MrBeast's channel ID
    if username:
        channel_id = get_channel_id_from_username(yt, username)
    channel_view_count_by_year(yt, channel_id)

if __name__ == "__main__":
    main()

