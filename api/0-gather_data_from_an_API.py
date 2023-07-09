#!/usr/bin/python3
"""This script retrieves todos for a specific user."""

import json
import requests
import sys

"""Imported modules to be used by the program"""

__author__ = "Junior"
if __name__ == '__main__':
    """Scripts to be executed"""
    user_id = sys.argv[1]
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    data = json.loads(response.text)
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id))
    result = json.loads(todos.text)
    done = 0
    total = 0
    itemArr = []

    for item in result:
        total += 1
        if item['completed']:
            done += 1
            itemArr.append(item['title'])

    print("Employee {} is done with ({}/{}) tasks"
        .format(data['name'], done, total))
    for item in itemArr:
        print("\t {}".format(item))
