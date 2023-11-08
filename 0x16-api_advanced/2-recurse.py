#!/usr/bin/python3
"""a recursive function that queries the `Reddit API` and returns a
list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return `None`.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively returns the titles of all hot articles"""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    if after:
        url += f"&after={after}"

    headers = {"User-Agent": "Chrome"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for post in data["data"]["children"]:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    return None
