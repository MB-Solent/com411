print("There are life cables to avoid. How many are there?")

cables_count = int(input())

avoided_amount = 0

while cables_count != 0:

    avoided_amount += 1

    print(f"Avoided {avoided_amount} cables!")

    cables_count -= 1
