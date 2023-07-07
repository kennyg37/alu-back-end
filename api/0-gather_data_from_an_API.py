#!/usr/bin/python3

""" 
The imported module of sys will help us take command-line arguments, and the requests module will help us access the get function.
"""

import sys
import requests

def get_employee_todo_progress(employee_id):
    """ 
    This function retrieves the TODO list progress for a given employee ID.
    """
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    if response.status_code == 200:
        todos = response.json()
        finished_tasks = []

        for todo in todos:
            if todo['completed'] == True:
                finished_tasks.append(todo)

        employee_name = todos[0]['username']
        all_tasks = len(todos)
        finished_tasks_count = len(finished_tasks)

        print(f"Employee {employee_name} is done with tasks ({finished_tasks_count}/{all_tasks}):")
        for task in finished_tasks:
            print(f"\t{task['title']}")

    else:
        print("No TODO list to fetch.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
