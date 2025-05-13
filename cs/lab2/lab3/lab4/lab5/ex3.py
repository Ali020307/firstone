# def find_max_difference(v, w):
#     max_diff = 0  # Initially, maximum difference is set to 0
#     max_index = -1  # Initially, no index has been found

#     # Loop over the elements of the arrays
#     for i in range(len(v)):
#         diff = abs(v[i] - w[i])  # Calculate the absolute difference
        
#         # If the current difference is greater than the previous maximum difference
#         if diff > max_diff:
#             max_diff = diff  # Update the maximum difference
#             max_index = i    # Update the index of maximum difference
    
#     return max_index, max_diff  # Return the index and the maximum difference


# def main():
#     # Step 1: Read the arrays from user input
#     v = []
#     w = []

#     # Input array v
#     print("Enter values for the first array (v):")
#     for i in range(10):
#         num = int(input(f"Input v[{i}]: "))
#         v.append(num)

#     # Input array w
#     print("Enter values for the second array (w):")
#     for i in range(10):
#         num = int(input(f"Input w[{i}]: "))
#         w.append(num)

#     # Step 2: Find the index and the maximum difference
#     index, difference = find_max_difference(v, w)

#     # Step 3: Display the results
#     print(f"The maximum absolute difference is {difference} at position {index}.")


# # Run the program
# if __name__ == "__main__":
#     main()
def find_dif(v, w):
    max_dif = 0
    max_index = -1
    for i in range(len(v)):
        dif = abs(v[i] - w[i])
        if dif > max_dif:
            max_dif = dif
            max_index = i
    return max_dif, max_index        
def main():
    v = []
    w = []
    print("enter values for the first array (v):")
    for i in range(10):
        num = int(input(f"input v[{i}]"))
        v.append(num)
    for i in range(10):
        num = int(input(f"input w[{i}]"))
        w.append(num)
    difference, index = find_dif(v, w)
    print(f"The maximum absolute difference is {difference} at position {index}.")
if __name__ == "__main__":
    main()