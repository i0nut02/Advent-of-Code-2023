import cmath
import math

def solve_quadratic_equation(a, b, c):
    delta = b**2 - 4*a*c

    if delta >= 0:
        root1 = (-b + (delta**0.5)) / (2*a)
        root2 = (-b - (delta**0.5)) / (2*a)
        return root1, root2
    else:
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(abs(delta)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

def product_of_ways_button(file):
    with open(file, mode="r") as f:
        content = f.read()
        time = int(content.split("\n")[0].split(":")[1].replace(" ", ""))
        distance = int(content.split("\n")[1].split(":")[1].replace(" ", ""))
    
    a, b = solve_quadratic_equation(-1, time, - distance)
    a, b = a +1 if a == int(a) else a, b-1 if b == int(b) else b
    
    return math.floor(b) - math.ceil(a) +1

print(product_of_ways_button("Day6/input.txt"))