#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
""" Library to gather data from an API """

import requests
import sys

""" Function to gather data from an API """

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todo = todo.format(employee_id)

    user_info = requests.request("GET", url).json()
    todo_info = requests.request("GET", todo).json()

    employee_name = user_info.get("name")
    total_tasks = list(filter(lambda x: (x["completed"] is True), todo_info))
    task_com = len(total_tasks)
    total_task_done = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          task_com, total_task_done))

    [print("\t {}".format(task.get("title"))) for task in total_tasks]
=======
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
>>>>>>> d15c26df69b7147cbfb0017309a9d0d2c1f9c8aa
=======
""" Library to gather data from an API """

import requests
import sys

""" Function to gather data from an API """

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todo = todo.format(employee_id)

    user_info = requests.request("GET", url).json()
    todo_info = requests.request("GET", todo).json()

    employee_name = user_info.get("name")
    total_tasks = list(filter(lambda x: (x["completed"] is True), todo_info))
    task_com = len(total_tasks)
    total_task_done = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          task_com, total_task_done))

    [print("\t {}".format(task.get("title"))) for task in total_tasks]
>>>>>>> 678aee67cd0bc8d16e3076503310b1f3893145ba
