print("the first line")
for i in range(10):
    for j in range(10):
        print(f"({i} , {j})", end=" ")
    print()
print("the second line")
for i in range(0, 100, 10):
    for j in range(i, i + 10):
         print(j, end=" ")   
    print()
