char = input("enter a character").lower()
if char in 'aeoui':
    print(f"the character '{char}' is a vowel ")
else:
    if char.isalpha():
        print(f"The character '{char}' is a consonant.")
    else:
        print("the input is not a letter")       