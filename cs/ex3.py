a = float(input("the first"))
b = float(input("the second"))
c = float(input("the third"))
if a >= b or a >= c :
    print(f"the first value ({a} is the largest)")
elif b >= a or b >= c  :
    print(f"the second value ({b}) is the largest one")
else: 
    print(f"the third value ({c}) is the largest one")
