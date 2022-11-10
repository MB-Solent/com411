def list_years(data):
    years = set()
    for row in data:
        years.add(row[9])
    for item in sorted(years, reverse=True):
        print(item)


def tally_medals(data):
    pass


def tally_team_medals(data):
    pass
