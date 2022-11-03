def observed():
    observations = []
    print("Please input observed items:")
    for i in range(5):
        item = input(f"Item {i+1}: ")
        observations.append(item)
    return observations


def remove_observations(observations):
    print("Do you want to remove an observations (Yes or No)?: ")

    remove = "Yes"
    valid = ("Yes", "No")

    while remove == "Yes":

        remove = input()

        while remove not in valid:

            print("Invalid choice. Choices are (Yes) and (No). Try again: ")
            remove = input()

        if remove == "Yes":


def run():
    print("Counting observations...")
    observations = observed()
    observations_count = set()

    for item in observations:
        observations_count.add((item, observations.count(item)))

    for count in observations_count:
        print(f"{count[0]} appeared {count[1]} time(s).")


if __name__ == "__main__":
    run()
