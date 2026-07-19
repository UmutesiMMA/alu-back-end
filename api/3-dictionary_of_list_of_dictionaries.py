#!/usr/bin/python3
"""
   exports data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    user_url = "https://jsonplaceholder.typicode.com/users/"
    user_data = requests.request("GET", user_url).json()
    jsonObject = {}
    for user in user_data:
        userId = user.get('id')
        todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        userId)
        todos = requests.request("GET", todo_url).json()
        assignedTodos=[]
        for todo in todos:
            todo_dict = {}
            todo_dict['username'] = user.get('username')
            todo_dict['task'] = todo.get('title')
            todo_dict['completed'] = todo.get('completed')
            assignedTodos.append(todo_dict)
        jsonObject[userId] = assignedTodos
       
    with open("{}.json".format(userId), 'w', newline='') as jsonfile:
            json.dump(jsonObject, jsonfile)
