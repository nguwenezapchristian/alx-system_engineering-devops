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

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data:
                print(post['data']['title'])
        else:
            print("No posts found in the subreddit.")
    else:
        print("None")
