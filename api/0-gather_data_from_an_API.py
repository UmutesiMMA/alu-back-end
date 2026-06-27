#!/usr/bin/python3
"""Get TODOs"""

import requests
import sys

if __name__ == '__main__':
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    user_data = requests.get(user_url)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(sys.argv[1])
    todos = requests.get(todos_url).json()
    completed_todos = list(filter(lambda todo:todo['completed'],todos))
    print('Employee {} is done with tasks({}/{}):'.format(user_data.json()['name'],len(completed_todos),len(todos)))
    for item in completed_todos:
        print('\t {}'.format( item['title']))