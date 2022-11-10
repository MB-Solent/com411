import csv


def started(msg=""):
    print("-"*85)
    print(f"Operation started:{msg}...")


def completed():
    print("\nOperation Completed")
    print("-"*85)


def error(msg):
    print(f"Error! {msg}")


def menu():
    print("Please Select one of the following options.")
    print(f"{'[years]':10}List unique years")
    print(f"{'[tally]':10}Tally up medals")
    print(f"{'[ctally]':10}Tally up medals for each team")
    print(f"{'[exit]':10}Exit the program")
    selection = input("Your Selection:")
    return selection


def display_medal_tally(tally):
    for medal,amount in tally.items():
        print(f"|{medal:10}|{amount:10}|")


def display_team_medal_tally(team_tally):
    for team, data in team_tally.items():
        print(f"{team}\n\t",end="")
        medals_string = ""
        for medal, amount in data.items():
            if medals_string != "":
                medals_string += ", "
            medals_string += f"{medal}:{amount}"
        print(f"{medals_string}")


def display_years(years):
    ascending = sorted(years, reverse=True)
    for year in ascending:
        print(year)

