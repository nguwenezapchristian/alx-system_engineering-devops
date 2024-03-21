#!/usr/bin/python3
import requests

def top_ten(subreddit):
    # Construct the URL for the subreddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Define a custom User-Agent to avoid errors related to Too Many Requests
    headers = {"User-Agent": "MyScript/1.0"}

    # Send a GET request to the API endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and retrieve the titles of the posts
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    elif response.status_code == 302:
        # Redirect response indicates an invalid subreddit
        print("None")
    else:
        # Other status codes may indicate errors or issues with the request
        print(f"Error: {response.status_code}")
