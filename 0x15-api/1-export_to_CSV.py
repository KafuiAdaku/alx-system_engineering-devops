#!/usr/bin/python3
"""A Python script to export data in the CSV format
    Requirements:
    *Records all tasks that are owned by this employee
    *Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    *File name must be: `USER_ID.csv`
"""
import csv
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
    employee_name = user["name"]

    with open(f"{employee_id}.csv", "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        # writer.writeheader()
        for todo in todos:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": todo['completed'],
                "TASK_TITLE": todo['title']
                })
