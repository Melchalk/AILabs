from math import sqrt

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 2 * a * c
    if a == 0:
        return -c / b
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        return ((-b - sqrt(discriminant)) / (2 * a),
                (-b + sqrt(discriminant)) / (2 * a))