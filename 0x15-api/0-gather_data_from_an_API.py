#!/usr/bin/python3
"""A Python script that returns information about an employee's TODO
list progress using this REST API.
Requirements:
*You must use urllib or requests module
*The script must display on the standard output the employee
TODO list progress in this exact format:
First line:
Employee EMPLOYEE_NAME is done with tasks
    (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the
    sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks:
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
import sys
import requests
import json

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

    total_task = len(todos)
    completed_tasks = sum(1 for todo in todos if todo["completed"])

    print(f"Employee {employee_name} is done with \
tasks({completed_tasks}/{total_task}):")
    for todo in todos:
        if todo["completed"]:
            print("\t " + todo["title"])
