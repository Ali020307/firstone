n = int(input("enter a positive number: "))
if n <= 0:
    print("print a positive int you jerk. ")
else:
    if n % 2 == 0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")