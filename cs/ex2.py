a =int(input("input the first number:"))
b =int(input("input the second number:"))
c =int(input("input the third number:"))

if a == b == c:
    print("all the three values are the same")

elif a == b or b == c or a == c:
    print("only two values have the same value")
else:
    print("no numbers have the same value")    