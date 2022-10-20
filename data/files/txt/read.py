def display_chars(file_path, char_number=1):

    with open(file_path) as file:

        partial_data = file.read(char_number)

        print("-" * 10)
        print(f"First {char_number} character(s) are:\n{partial_data}")


def display_line(file_path):

    with open(file_path) as file:

        first_line = file.readline()
        print("-"*10)
        print(f"The first line is:\n{first_line}.")


def display_text(file_path):

    with open(file_path) as file:

        print("-" * 10)
        print(f"The full file is:\n{file.read()}")


def run():

    display_text("library.txt")
    display_chars("library.txt", 5)
    display_line("library.txt")


if __name__ == "__main__":
    run()
