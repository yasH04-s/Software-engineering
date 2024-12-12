import math
import cmath

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)  # Two real and different roots
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
    elif discriminant == 0:
        root1 = root2 = -b / (2*a)  # Two real and identical roots
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)  # Two complex roots
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2

# Function to predict the temperature at time x
def predict_temperature(a, b, c, x):
    return a * x**2 + b * x + c  # Using the quadratic equation to calculate temperature

# Function to process the equation from a file
def process_single_equation_from_file(filename):
    try:
        with open(filename, 'r') as file:
            a = float(file.readline().strip())  # Read the lines and convert to float
            b = float(file.readline().strip())
            c = float(file.readline().strip())

            root1, root2 = solve_quadratic(a, b, c)
            
            time = 15
            temperature_at_3pm = predict_temperature(a, b, c, time)

            print(f"The quadratic equation: T(x) = {a}x^2 + {b}x + {c}")
            print(f"Roots of the equation: {root1}, {root2}")
            print(f"Predicted temperature at 3 PM (x = {time}): {temperature_at_3pm:.2f} °C")
    
    except FileNotFoundError:
        print("Error: The file was not found.")
    except ValueError:
        print("Error: There was an issue with reading the coefficients from the file.")
    except Exception as e:
        print(f"An error occurred: {e}") 

process_single_equation_from_file('input.txt')