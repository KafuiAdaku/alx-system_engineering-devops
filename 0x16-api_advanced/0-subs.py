#!/usr/bin/python3
"""A function that queries the `Reddit API` and returns the number of
subscibers for a given subreddit.
If an invalid subreddit is given the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Qeuries a reddit api for the number of subscibers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Chrome"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()

        subscribers = data["data"]["subscribers"]
        return subscribers
    return 0
