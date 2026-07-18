#!/usr/bin/python3
"""Get TODOs"""

import json

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todo = todo.format(employee_id)

    user_data = requests.request("GET", url).json()
    todos = requests.request("GET", todo).json()

    employee_name = user_data.get("name")
    total_tasks = list(filter(lambda x: (x["completed"] is True), todos))
    task_com = len(total_tasks)
    total_task_done = len(todos)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, task_com, total_task_done
        )
    )
    [print("\t {}".format(task.get("title"))) for task in total_tasks]
