# def floyds_triangle(n):
#     num = 1  # Start the first number
#     for i in range(1, n + 1):  # Loop through each row
#         for j in range(i):  # Loop through elements in the current row
#             print(num, end=" ")  # Print the current number
#             num += 1  # Increment the number for the next element
#         print()  # Move to the next line after each row

# # Read the number of rows from the user
# n = int(input("Enter the number of rows for Floyd's Triangle: "))
# floyds_triangle(n)
n = int(input("the value of number of rows:"))

num = 1
for i in range(0, n):
    for j in range(0, i + 1):
        print(num, end=" ")
        num += 1
    print()    
