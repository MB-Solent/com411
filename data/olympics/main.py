import csv
import process
import tui


def read_data(file_path):
    tui.started(f"Reading data from {file_path}")
    data = []
    with open("athlete_events.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        next(reader, None)
        for row in reader:
            data.append(row)
    tui.completed()
    return data


def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            tui.started("listing all the years with olympic years.")
            process.list_years(athlete_data)
            tui.completed()
        elif selection == "tally":
            tui.started("tallying up all medals.")
            process.tally_medals(athlete_data)
            tui.completed()
        elif selection == "team":
            tui.started("tallying up all medals for each individual country.")
            process.tally_team_medals(athlete_data)
            tui.completed()
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()