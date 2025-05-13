area = 0.0

def square(a):
    area = a ** 2
    return area

def rectangle(length, width):
    area = length * width
    return area

def triangle(height, base):
    area = height * base / 2
    return area

def circle(radius):
    area = 3.14 * radius ** 2
    return area


print("Square area:", square(5))
print("Rectangle area:", rectangle(5, 6))
print("Triangle area:", triangle(4, 6))
print("Circle area:", circle(4))

