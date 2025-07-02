from math import sqrt

# Get coordinates for the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Get coordinates for the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance using the distance formula: d = √[(x₂-x₁)² + (y₂-y₁)²]
distance_squared = (x2 - x1)**2 + (y2 - y1)**2
distance = sqrt(distance_squared)

print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")