#!/usr/bin/python3
"""Write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search for.

    Returns:
        None
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {"User-Agent": "Chris-User-Agent"}

    sub_info = requests.get(url,
                            headers=headers,
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]
