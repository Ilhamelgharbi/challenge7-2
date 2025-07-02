def calculation(a: float, b: float) -> tuple[float, float]:
    return a + b, a - b
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

somme, difference = calculation(a, b)
print(f"Sum: {somme}")
print(f"Difference: {difference}")

