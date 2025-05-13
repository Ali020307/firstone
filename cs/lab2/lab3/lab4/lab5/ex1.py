N = int(input("enter the number of values"))
v = []
print(f"pleas enter {N} positive values:")

for i in range(N):
    num = int(input(f"enter number {i + 1}: "))
    v.append(num)

odd_number = []    
even_number = []

for num in v:
    if num % 2 == 0:
        even_number.append(num)
    else:
        odd_number.append(num)

print(f"the even numbers:", *even_number)
print(f"the odd numbers:", *odd_number)