#!/usr/bin/python3
"""Get TODOs"""

import json

import requests
import sys

if __name__ == '__main__':
    user_url = ("https://jsonplaceholder.typicode.com/users/{}".
                format(sys.argv[1]))
    user_data = requests.get(user_url).json()
    user_name = user_data.get('name')
    todos_url = ("https://jsonplaceholder.typicode.com/todos?userId={}".
                 format(sys.argv[1]))
    todos = requests.get(todos_url).json()
    completed_todos = list(filter(lambda todo: todo['completed'], todos))
    print('Employee {} is done with tasks({}/{}):'.format(
        user_name,
        len(completed_todos),
        len(todos)))
    for item in completed_todos:
        print('\t {}'.format(item.get('title')))
