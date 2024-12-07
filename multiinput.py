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

def process_multiple_equations(filename):
    with open(filename, 'r') as file:
        while True:
            try:
                a = float(file.readline().strip())
                b = float(file.readline().strip())
                c = float(file.readline().strip())
                
                root1, root2 = solve_quadratic(a, b, c)
                print(f"The roots for a={a}, b={b}, c={c} are: {root1}, {root2}")
            except ValueError:
                break
process_multiple_equations('input.txt')