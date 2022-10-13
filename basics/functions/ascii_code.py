print("Program Started!")

letter = input("Please enter a standard character:")

if len(letter) == 1:
    ascii_code = ord(letter)
    print(f"The ASCII code for {letter} is {ascii_code}")

else:
    print("That's not a single character.")
