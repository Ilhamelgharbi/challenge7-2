
#challenge 2
name= input("enter your name : ")
salary= float(input("enter your hourly salary : "))
hours= float(input("enter the number of the hour that you worked : "))
if (hours) > 40:
    overtime = int(hours) - 40
    overtimesalary = overtime * (float(salary) * 1.5)
    totalsalary = (40 * float(salary)) + overtimesalary
    print(f" {name} Your total pay is: {totalsalary} dhs")
else:
    totalsalary = (hours) * float(salary)
    print(f" {name} Your total pay is: {totalsalary} dhs")