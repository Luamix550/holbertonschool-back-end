#!/usr/bin/python3
"""

"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    all_tasks = {}
    
    for user in users:
        user_id = str(user['id'])
        username = user['username']
        user_tasks = []
        
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        response = requests.get(url)
        tasks = response.json()
        
        for task in tasks:
            user_tasks.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })
        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
