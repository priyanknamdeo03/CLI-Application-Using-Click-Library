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

    with open('employee.json', 'r') as file:
        data = json.load(file)

    data.append(entity)
    with open('employee.json', 'w') as file:
        json.dump(data, file, indent=4)


@click.command(name='view_employee', help='Display all entries in Employee')
def view_employees():
    with open('employee.json', 'r') as file:
        data = json.load(file)
    
    for fetch_details in data:
        click.echo("-------------------------------")
        print("Employee Name : ", fetch_details['name'])
        print("Employee Id : ", fetch_details['id'])
        print("Employee Department : ", fetch_details['department'])
        click.echo("-------------------------------")


@click.command(name='delete_employee', help='Delete entry in Employees table')
@click.option('--id', prompt='Enter Id of Employee To Delete', help='Employee Id', type=int)
def delete_employee(id):
    click.echo("\n--- Delete Employee ---")
    
    with open(f'employee.json', "r+", encoding="utf-8") as file:
        data = json.load(file)
        
        for row_detail in range(len(data)):
            if data[row_detail]['id'] == id:
                del data[row_detail]
                click.echo("\Record Deletion Successful.............\n")
                break
        else:
            click.echo("\nId not found in our database...........\n")
    
    with open(f'employee.json', "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


@click.group(help='Commands for managing employee database')
def employee():
    pass

employee.add_command(add_employee)
employee.add_command(view_employees)
employee.add_command(delete_employee) 


if __name__ == '__main__':
    employee()
    















