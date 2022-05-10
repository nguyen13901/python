from item import Item
from employee import Employee

import datetime

item1 = Item("MyItem", 50, 5)
print(item1.name)
item1.name = "Phone"
print(item1.name)

# ==================
# class, static method
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_2.email)
print(new_emp_2.pay)
print(new_emp_3.email)
print(new_emp_3.pay)

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

# special, dunder method

print(len(emp_1))
print(emp_1 + emp_2)

# Property, setter, deleter

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
