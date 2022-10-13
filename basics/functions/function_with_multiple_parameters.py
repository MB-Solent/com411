def climb_ladder(already_climbed, left_to_climb):

    if already_climbed <= left_to_climb:
        print("Still some left to go!")

    else:
        print("We are almost there!")


climb_ladder(2, 3)
climb_ladder(3, 3)
climb_ladder(4, 3)
