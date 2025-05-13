n = int(input("enter the number of values of the sequence (at least 2):"))
if n < 2:
    print("the number of values has to be at least 2")
else:
    values = []
    for i in range(n):
        value = float(input(f"enter value {i + 1}:"))
        values.append(value)
    largest = max(values)
    values.remove(largest)
    second_largest  = max(values)
    
    print(f"the largest value is {largest} and the second largest value is {second_largest}" )