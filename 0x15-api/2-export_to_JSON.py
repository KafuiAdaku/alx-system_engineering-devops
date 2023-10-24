#!/usr/bin/python3
"""A Python script to export data in the JSON format
    Requirement:
        *Records all tasks that are owned by this employee
        *Format must be: { "USER_ID":
        [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username":
        "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
        "username": "USERNAME"}, ... ]}
        *File name must be: USER_ID.json
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    todos_url = f"https://jsonplaceholder.typicode.com/users/\
{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos = json.loads(todos_response.text)

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user = json.loads(user_response.text)
    username = user["username"]

    export_dict = {}
    my_list = []

    for todo in todos:
        my_dict = {}
        my_dict["task"] = todo['title']
        my_dict["completed"] = todo["completed"]
        my_dict["username"] = username
        my_list.append(my_dict)

    export_dict[employee_id] = my_list

    with open(f"{employee_id}.json", "w", encoding="utf-8") as f:
        json.dump(export_dict, f)
