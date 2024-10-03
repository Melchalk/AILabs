def get_type_triangle_by_angles(a, b, c):
    if a > 90 or b > 90 or c > 90:
        return "тупоугольный"
    elif a == 90 or b == 90 or c == 90:
        return "прямоугольный"
    else:
        return "остроугольный"

def get_type_triangle_by_sides(ab, bc, ca):
    if ab == bc == ca:
        return "равносторонний"
    elif ab == bc or bc == ca or ab == ca:
        return "равнобедренный"
    else:
        return "разносторонний"

def get_type_triangle(a, b, c, ab, bc, ca):
    type_by_angles = get_type_triangle_by_angles(a, b, c)
    type_by_sides = get_type_triangle_by_sides(ab, bc, ca)
    return type_by_sides + "-" + type_by_angles



