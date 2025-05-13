def triangle(a, b, c):
    if a< b + c and b < a + c and c < b + a:
        if a == b == c:
            return "Equilateral triangle"
        elif a == b or b == c or c == b:
            return "Isosceles triangle"
        elif a != b != c:
            if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
                return "Scalene Right-Angled Triangle"
            else:
                return "Scalene triangle"
    else:
        return "The sides do not form a valid triangle" 


a = float(input("enter a"))           
b = float(input("enter b"))           
c = float(input("enter c")) 

result = triangle(a, b, c)
print(result)
