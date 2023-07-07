#!/usr/bin/python3s
""" the imported module of sys will help as take 
command-line arguments and the request odule will help us
access the get, post functions
"""
import sys
import requests

def get_employee_todo_progress(employee_id):
    """ this function holds the parameter employee_id so that in case
    we choose to use a function rather than a command-line argument
    the code works"""
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

        print(f"Employee {employee_name} is done with tasks ({completed_task_count}/{total_tasks}):")
        for task in finished_tasks:
            print(f"\t{task['title']}")

    else:
        print("no TODO list to fetch")
if __name__ == "__main__":
        if len(sys.argv) > 1:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        else:
            print("no parameter is provided")
