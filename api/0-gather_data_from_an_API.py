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
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    )
    data = json.loads(response.text)
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos/'
    )
    result = json.loads(todos.text)
    done = 0
    total = 0
    item_arr = []

    for item in result:
        if data['id'] == item['userId']:
            total += 1
            if item['completed']:
                done += 1
                item_arr.append(item['title'])

    print("Employee {} is done with ({}/{})".format(data['name'], done, total))
    for item in item_arr:
        print("\t{}".format(item))
