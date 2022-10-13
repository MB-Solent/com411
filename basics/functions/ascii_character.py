print("Program Started!")

print("Please enter an ASCII code:", end="")

ascii_code = int(input())

ascii_range = range(32, 126+1)

if abs(ascii_code) == ascii_code and ascii_code in ascii_range:
    ascii_character = chr(ascii_code)
    print(f"The character represented by the ASCII code {ascii_code} is {ascii_character}")

else:
    print("That is not a valid number.")
