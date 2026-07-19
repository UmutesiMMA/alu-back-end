#!/usr/bin/python3
"""
   exports data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    user_data = requests.request("GET", user_url).json()
    todos = requests.request("GET", todo_url).json()
    user_name = user_data.get('username')
    assignedTodos = []
    for todo in todos:
        todo_dict = {}
        todo_dict['task'] = todo_url.get('title')
        todo_dict['completed'] = todo_url.get('completed')
        todo_dict['username'] = user_name
        assignedTodos.append(todo_dict)
    jsonObject = {}
    jsonObject[employee_id] = assignedTodos
    with open("{}.json".format(employee_id), 'w', newline='') as jsonfile:
        json.dump(jsonObject, jsonfile)
