def main():
    while True:

        n = int(input("the number of values:"))
        if n <= 0 or n > 100:
            print("the n cannot be negative or greaterthan 100")
            continue


        v = []
        for i in range(n):
            num = int(input(f"input v[{i}]:"))
            v.append(num)
        x = int(input("input x: "))
        count = v.count(x)
        print(f"value {x} appears {count} time(s) in the array.")

        repeat = int(input("would tou like to continue? "))
        if repeat == False:
            print("program terminated.")
            break
main()


# def main():
#     while True:
#         # Step 1: Read a positive integer n (size of the array)
#         n = int(input("Input n: "))
        
#         # Ensure n is positive and within the specified range
#         if n <= 0 or n > 100:
#             print("Please enter a valid number of elements (1 <= n <= 100).")
#             continue
        
#         # Step 2: Load the array v of n integers
#         v = []
#         for i in range(n):
#             num = int(input(f"Input v[{i}]: "))
#             v.append(num)
        
#         # Step 3: Read an integer x to search for in the array
#         x = int(input("Input x: "))
        
#         # Step 4: Determine how many times x appears in the array
#         count = v.count(x)
        
#         # Print the result
#         print(f"Value {x} appears {count} time(s) in the array.")
        
#         # Step 5: Ask if the user wants to continue
#         repeat = int(input("Would you like to continue (1=yes, 0=no)? "))
        
#         if repeat == 0:
#             print("Program terminated.")
#             break  # Exit the loop and terminate the program

# # Run the program
# main()
