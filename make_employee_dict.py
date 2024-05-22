# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# NOTE: Will not have a ReadMe - Using another IDE
# Date: 05/22/2024
# Description: Program that creates an Employee object from an Employee class and uses the ID number as a key to show Employee information

class Employee:
    def __init__(self, name, ID_number, salary, email_address):
        '''Function that initializes name, ID number, salary, and email address'''
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        '''function that returns the name'''
        return self._name

    def get_ID_number(self):
        '''function that returns the ID number'''
        return self._ID_number

    def get_salary(self):
        '''function that returns the salary'''
        return self._salary

    def get_email_address(self):
        '''function that returns the email address'''
        return self._email_address

def make_employee_dict(names, ids, salaries, emails):
    '''function that creates a dictionary from employee objects'''
    employee_dict = {}
    for i in range(len(names)):
        employee = Employee(names[i], ids[i], salaries[i], emails[i])
        employee_dict[ids[i]] = employee
    return employee_dict

# names = ["Jean", "Kat", "Pomona"]
# ids = ["100", "101", "102"]
# salaries = [30, 35, 28]
# emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]

# employees = make_employee_dict(names, ids, salaries, emails)
# print(employees["101"].get_name())
