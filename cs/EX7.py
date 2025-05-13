# Read year from the user
year = int(input("Enter a year: "))  # Convert input to an integer

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
