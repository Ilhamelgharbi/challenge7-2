
#challenge 3
while True:
    try:
        name= input("enter your name")
        salary= float(input("enter your hourly salary"))
        hours=float(input("enter the number of the hour that you worked :"))
        if hours > 40:
            overtime = hours - 40
            overtimesalary = overtime * (salary * 1.5)
            totalsalary = (40 * salary) + overtimesalary
            print(f" {name} Your total pay is: {totalsalary} dhs")
        else:
            totalsalary = hours * salary
            print(f" {name} Your total pay is: {totalsalary} dhs")
    except ValueError:
        print("Please enter valid numeric values for salary and hours.")