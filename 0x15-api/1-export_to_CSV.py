#!/usr/bin/python3
""" Gather data from an API and export to csv"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + f"users/{userId}").json()
    todos = requests.get(url + f"todos?userId={userId}").json()
    USERNAME_NAME = user.get("username")
    with open(f"{userId}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                    [
                        userId,
                        USERNAME_NAME,
                        task.get("completed"),
                        task.get("title")
                        ]
                    )
