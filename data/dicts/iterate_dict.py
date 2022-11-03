import simple_dict


def display_keys(data):
    for key in data.keys():
        print(key)


def display_values(data):
    for value in data.values():
        print(value)


def display_items(data):
    for key, value in data.items():
        print(f"{key}: {value}")


def run():
    display_keys(simple_dict.pattern())
    display_values(simple_dict.pattern())
    display_items(simple_dict.pattern())


if __name__ == "__main__":
    run()

