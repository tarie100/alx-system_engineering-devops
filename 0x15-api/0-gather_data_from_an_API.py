#!/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
    base_url = 'https://api.example.com/'
    employee_url = base_url + 'employees/' + str(employee_id)
    todos_url = base_url + 'todos?employeeId=' + str(employee_id)

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        if employee_response.status_code == 200 and todos_response.status_code == 200:
            employee_data = employee_response.json()
            todos_data = todos_response.json()

            employee_name = employee_data['name']
            total_tasks = len(todos_data)
            done_tasks = sum(1 for todo in todos_data if todo['completed'])

            print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")

            for todo in todos_data:
                if todo['completed']:
                    print(f"\t {todo['title']}")

        else:
            print("Error: Unable to retrieve employee and/or TODO data.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

