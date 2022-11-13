import tui


def list_years(data):
    years = set()
    for row in data:
        years.add(row[9])

    tui.display_years(years)


def tally_medals(data):
    medals = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for entry in data:
        for medal in medals.keys():
            if entry[14] == medal:
                medals[medal] += 1

    tui.display_medal_tally(medals)


def tally_team_medals(data):
    team_medals = {}
    print(type(team_medals))
    # medals = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for entry in data:
        if entry[6] in team_medals:
            for medal in team_medals[entry[6]].keys():
                if entry[14] == medal:
                    team_medals[entry[6]][medal] += 1
        else:
            team_medals[entry[6]] = {"Gold": 0, "Silver": 0, "Bronze": 0}

    tui.display_team_medal_tally(team_medals)


