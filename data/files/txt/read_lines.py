def search():
    print(f"Searching...")
    with open("library.txt") as file:
        for line in file:
            print(f"Searched in {line}", end="")
        print("\nDone!")


def run():
    search()


if __name__ == "__main__":
    run()
