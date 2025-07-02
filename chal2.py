
#challenge 2
name= input("enter your name");
salary= input("enter your hourly salary");
hours= input("enter the number of the hour that you worked :");
if int(hours) > 40:
    overtime = int(hours) - 40
    overtimesalary = overtime * (float(salary) * 1.5)
    totalsalary = (40 * float(salary)) + overtimesalary
    print(f" {name} Your total pay is: {totalsalary} dhs")
else:
    totalsalary = int(hours) * float(salary)
    print(f" {name} Your total pay is: {totalsalary} dhs")