import click
import json


@click.command(name='add_employee', help='Create entry in Employees table')
@click.option('--name', prompt='Enter name of Employee ', help='Employee Name', type=str)
@click.option('--id', prompt='Enter Id of Employee ', help='Employee Id', type=int)
@click.option('--department', prompt='Enter department of Employee ', help='Department', type=str)
def add_employee(**options):
    entity = {
        'name': options['name'].lower(),
        'id': options['id'],
        'department': options['department'],
    }

    with open('student.json', 'r') as file:
        data = json.load(file)

    data.append(entity)
    with open('student.json', 'w') as file:
        json.dump(data, file, indent=4)


@click.command(name='view_employee', help='Display all entries in Employee')
def view_employees():
    with open('student.json', 'r') as file:
        data = json.load(file)
    
    for fetch_details in data:
        print("-------------------------------")
        print("Employee Name : ", fetch_details['name'])
        print("Employee Id : ", fetch_details['id'])
        print("Employee Department : ", fetch_details['department'])
        print("-------------------------------")


@click.command(name='delete_employee', help='Delete entry in Employees table')
@click.option('--id', prompt='Enter Id of Employee To Delete', help='Employee Id', type=int)
def delete_employee(id):
    print("\n--- Delete Student ---")
    
    with open(f'student.json', "r+", encoding="utf-8") as file:
        data = json.load(file)
        
        for row_detail in range(len(data)):
            if data[row_detail]['id'] == id:
                del data[row_detail]
                print("\Record Deletion Successful.............\n")
                break
        else:
            print("\nId not found in our database...........\n")
    
    with open(f'student.json', "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


@click.group(help='Commands for managing employee database')
def employee():
    pass

employee.add_command(add_employee)
employee.add_command(view_employees)
employee.add_command(delete_employee) 


if __name__ == '__main__':
    employee()
    















