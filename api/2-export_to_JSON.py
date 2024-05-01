import requests
import json
from sys import argv

if __name__ == "__main__":

    id = int(argv[1])

    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}?_embed=todos')
    all_data = response.json()

    username = all_data.get("username")

    tasks = all_data.get("todos", [])

    json_data = {str(id): []}
    for task in tasks:
        json_data[str(id)].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        })

    filename = f"{id}.json"
    with open(filename, "w") as file:
        json.dump(json_data, file)