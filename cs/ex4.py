def calculate(x, y, z):
    if x == '+':
        return y + z
    elif x == '-':
        return y - z
    elif x == '*':
        return y * z
    elif x == '/':
        if x != 0:
            return y / z
        else:
            return "ERROR"
    else:
        return "INVALID OPERATOR"   
expression = input("input expressions:") 
parts = expression.split()
x = parts[0]     
y = float(parts[1])
z = float(parts[2])
result = calculate(x, y, z)
print(f"operation result:{y} {x} {z} = {result}")

