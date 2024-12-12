import math
import cmath

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
    elif discriminant == 0:
        root1 = root2 = -b / (2*a)
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2

def predict_temperature(a, b, c, x):
    return a * x**2 + b * x + c

def process_multiple_equations(filename):
    with open(filename, 'r') as file:
        while True:
            try:
                a = float(file.readline().strip())
                b = float(file.readline().strip())
                c = float(file.readline().strip())
                
                root1, root2 = solve_quadratic(a, b, c)
                
                time = 15 
                temperature_at_3pm = predict_temperature(a, b, c, time)
                
                print(f"The quadratic equation: T(x) = {a}x^2 + {b}x + {c}")
                print(f"Roots of the equation: {root1}, {root2}")
                print(f"Predicted temperature at 3 PM (x = {time}): {temperature_at_3pm:.2f} °C\n")
            except ValueError:
                break
process_multiple_equations('input2.txt')