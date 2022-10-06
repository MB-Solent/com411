print("How many bars should be charged?")

max_bars = int(input())

current_bars = 0

while current_bars < max_bars:
    current_bars += 1
    print("Charging:"+"█"*current_bars)

