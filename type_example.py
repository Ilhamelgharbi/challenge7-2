# Demonstrating Python's dynamic typing

# When you assign values, Python automatically determines types
salary = 25.5        # Python knows this is a float
hours = 45           # Python knows this is an int
name = "John"        # Python knows this is a string

print(f"salary type: {type(salary)}")
print(f"hours type: {type(hours)}")
print(f"name type: {type(name)}")

# When you do calculations, Python determines the result type
overtime = hours - 40                    # int - int = int
overtimesalary = overtime * (salary * 1.5)  # int * (float * float) = float
totalsalary = (40 * salary) + overtimesalary # (int * float) + float = float

print(f"overtime type: {type(overtime)}")
print(f"overtimesalary type: {type(overtimesalary)}")
print(f"totalsalary type: {type(totalsalary)}")

# You can even change a variable's type during runtime!
my_var = 10          # int
print(f"my_var is: {my_var}, type: {type(my_var)}")

my_var = "Hello"     # now it's a string
print(f"my_var is: {my_var}, type: {type(my_var)}")

my_var = 3.14        # now it's a float
print(f"my_var is: {my_var}, type: {type(my_var)}")
