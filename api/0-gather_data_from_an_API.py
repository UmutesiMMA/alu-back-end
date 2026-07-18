#!/usr/bin/python3
"""Get TODOs"""

import json

import requests
import sys

if __name__ == '__main__':
    user_url = ("https://jsonplaceholder.typicode.com/users/{}".
                format(sys.argv[1]))
    user_data = requests.get(user_url)
    todos_url = ("https://jsonplaceholder.typicode.com/users/{}/todos".
                 format(sys.argv[1]))
    todos = json.loads(requests.get(todos_url).text)
    completed_todos = list(filter(lambda todo: todo['completed'], todos))
    print('Employee {} is done with tasks({}/{}):'.format(
        json.loads(user_data.text)['name'],
        len(completed_todos),
        len(todos)))
    for item in completed_todos:
        print('\t {}'.format(item['title']))
