#!/usr/bin/python3
"""
script to export data in the CSV format
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    id = int(argv[1])

    emp_r = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    all_data = emp_r.json()
    username = all_data.get("username")

    t = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    tasks = t.json()

    filename = f"{id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, dialect="unix")
        for task in tasks:
            completed_status = "True" if task["completed"] else "False"
            writer.writerow([id, username, completed_status, task["title"]])
