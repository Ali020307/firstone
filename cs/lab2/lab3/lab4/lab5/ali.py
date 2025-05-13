import random

secret_number = random.randint(1, 10)  # Random number between 1-10
attempts = 5  # Total allowed guesses
guess = None
try:
    print("You have 3 attempts to guess the secret number (1-10).")
    while attempts > 0:
        guess = int(input("input number "))
        if guess == secret_number:
            print("congrats you have won")
            break
        elif guess > secret_number:
            print("too high")
        else:
            print("too low")
        attempts -= 1
        print(f"only {attempts} left")
    if attempts == 0 and guess != secret_number:
        print(f"you are a loser the number is {secret_number}")   
except:
    print("only numbers")