#!/usr/bin/python3
""" Gather data from an API and export to json"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + f"users/").json()
    todo_all_employees = {}
    for user in users:
        userId = str(user.get("id"))
        USERNAME_NAME = user.get("username")
        todos = requests.get(url + f"todos?userId={userId}").json()
        user_tasks = []
        for task in todos:
            user_tasks.append({
                "username": USERNAME_NAME,
                "task": task.get("title"),
                "completed": task.get("completed")
                })
        todo_all_employees[userId] = user_tasks
    with open(f"todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_all_employees, jsonfile)
