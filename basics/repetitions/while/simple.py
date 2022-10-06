print("How many cables are there to remove?")

cable_count = int(input())

while cable_count != 0:
    cable_count -= 1
    print("Removing a cable")
    print(f"There are {cable_count} left.")

print("All cables are gone.")
