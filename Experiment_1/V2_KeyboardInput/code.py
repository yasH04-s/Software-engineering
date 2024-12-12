# to get user input for coefficients
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
# to calculate discriminant
discriminant = b**2 - 4*a*c
# to sheck if roots are real
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots are: {root1} and {root2}")
else:
    print("No real roots exist.")
