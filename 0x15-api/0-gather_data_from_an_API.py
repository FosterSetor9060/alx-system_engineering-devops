#!/usr/bin/python3
"""
For the script, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        sys.exit(1)
    user = user_response.json()
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error fetching todos.")
        sys.exit(1)
    todos = todos_response.json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for complete in completed:
        print("\t {}".format(complete))

