def directions():
    direction_list = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction_list


def menu():
    print("Please select a direction: ")
    directions_list = directions()
    for item in directions_list:
        print(f"{directions_list.index(item)}: {item}")
    pass


def run():
    menu()
    pass


if __name__ == "__main__":
    run()
