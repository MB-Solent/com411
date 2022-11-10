import matplotlib.pyplot as plt


def small():
    x = [3, 3, 4, 4, 3]
    y = [3, 4, 4, 3, 3]
    plt.plot(x, y, 'ro--')


def medium():
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]
    plt.plot(x, y, 'gs--')


def run():
    small()
    medium()
    plt.show()


if __name__ == "__main__":
    run()
