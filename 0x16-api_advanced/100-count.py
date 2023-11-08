#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces).
"""
import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Returns a sorted count of given keywords"""
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    if after:
        url += f"&after={after}"

    headers = {"User-Agent": "My Custom Header"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        children = data.get("data").get("children")
        for post in children:
            title = post.get("data").get("title").lower()
            for word in word_list:
                if re.search(fr"\b{re.escape(word)}\b", title):
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1
        after = data.get("data").get("after")
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            srt_cnt = sorted(counts.items(),
                             key=lambda x: (-x[1], x[0].lower()))
            for keyword, count in srt_cnt:
                print(f"{keyword.lower()}: {count}")
