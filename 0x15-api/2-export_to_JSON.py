#!/usr/bin/python3
""" Gather data from an API and export to json"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + f"users/{userId}").json()
    todos = requests.get(url + f"todos?userId={userId}").json()
    USERNAME_NAME = user.get("username")
    with open(f"{userId}.json", "w") as jsonfile:
        for task in todos:
            json.dump(
                    {userId: [{
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": USERNAME_NAME
                        }]
                        }
                    ,jsonfile)
