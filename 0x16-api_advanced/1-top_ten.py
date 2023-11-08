#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Returns top 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Chrome"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()

        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
