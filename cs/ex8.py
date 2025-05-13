import math

# Read the coefficients a, b, and c from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the discriminant and calculate the roots accordingly
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots are real and distinct: {root1} and {root2}")
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2 * a)
    print(f"The root is real and repeated: {root}")
else:
    # Complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
