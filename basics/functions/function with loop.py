def cross_bridge(bridge_length):
    for _ in range(bridge_length):
        print("Crossed step.")

    if bridge_length >= 6:
        print("The bridge is collapsing!")

    else:
        print("We must keep going!")


cross_bridge(3)
cross_bridge(6)
