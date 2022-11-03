def observed():
    observations = []
    print("Please input observed items:")
    for i in range(7):
        item = input(f"Item {i+1}: ")
        observations.append(item)
    return observations
    pass


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
