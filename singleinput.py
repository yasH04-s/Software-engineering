import math
a = 5
b = -0.2
c = 0

discriminant = b**2 - 4*a*c
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots are: {root1} and {root2}")
else:
    print("No real roots.")