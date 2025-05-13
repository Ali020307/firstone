def main():
    while True:
        # Read an integer number n
        n = int(input("Input n: "))
        
        # Check if n is positive
        if n > 0:
            print('*' * n)  # Display n asterisks in one row
        else:
            print("Execution terminated.")  # Terminate the program
            break  # Exit the loop and stop the program
if __name__ == "__main__":
    main()
