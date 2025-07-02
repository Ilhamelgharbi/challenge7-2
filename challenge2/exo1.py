def horaire_supp (hours :float  , salary :float , name :str) -> float:
    if int(hours) > 40:
        overtime = int(hours) - 40
        overtimesalary = overtime * (salary * 1.5)
        totalsalary = (40 * salary) + overtimesalary
        return totalsalary
    else:
        totalsalary = int(hours) * salary
        return totalsalary
name= input("enter your name : ")
salary= float(input("enter your hourly salary : "))
hours= float(input("enter the number of the hour that you worked : "))
totalsalary = horaire_supp(hours, salary, name)
print(f" {name} Your total pay is: {totalsalary} dhs")