def display_ladder(steps_count):
    for _ in range(steps_count):
        print("╬═══╬")


def create_ladder():
    print("How many steps are there left to climb?")

    step_count = 0

    while True:

        user_input = input()

        try:

            step_count = int(user_input)

            if step_count > 0:
                display_ladder(step_count)
                break

            else:
                print("Input a number bigger than 0. Try again.")

        except ValueError:
            print("That is not a valid step number. Try again")

create_ladder()
