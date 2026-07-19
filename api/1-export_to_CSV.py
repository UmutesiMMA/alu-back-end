#!/usr/bin/python3
"""
   exports data in the CSV format
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user_data = requests.request("GET", user_url).json()
    todos = requests.request("GET", todo_url).json()

    with open("{}.csv".format(employee_id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            taskwriter.writerow([int(employee_id), user_data.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
