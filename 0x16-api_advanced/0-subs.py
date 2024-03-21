#!/usr/bin/python3
""" a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0 """
import requests


def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit
    API and returns the number of subscribers
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "0x16-api_advanced (nguwenezacc982@gmail.com)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 400:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
