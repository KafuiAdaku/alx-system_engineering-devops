#!/usr/bin/python3
"""A Python script to export data in the JSON format.
    Requirments:
    *Records all tasks from all employees
    File name must be: todo_all_employees.json
"""
import json
import requests

if __name__ == "__main__":

    users_url = f"https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = json.loads(users_response.text)

    todos_dict = {}
    for user in users:
        user_id = user["id"]
        username = user["username"]

        todos_url = f"https://jsonplaceholder.typicode.com/todos?\
userId={user_id}"
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        task_list = []
        for todo in todos:
            task = {
                    "username": username,
                    "task": todo["title"],
                    "completed": todo["completed"]
                    }
            task_list.append(task)

        todos_dict[user_id] = task_list

    print(todos_dict)
