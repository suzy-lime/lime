# CHESS BOARD :)
rows = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

# SET UP TEST CASES AND WHILE LOOP
t_cases = int(input("How many test cases will there be? "))

while t_cases > 0:
    # INPUT LOCATIONS
    bishop_start = input("Where does the bishop start? ")
    pawn_start = input("Where does the pawn start? ")

    # SPILT STRINGS
    bishop_location = [x for x in bishop_start]
    pawn_location = [x for x in pawn_start]

    bishop_location[0] = rows[bishop_location[0]]
    pawn_location[0] = rows[pawn_location[0]]

    bishop_location[1] = int(bishop_location[1])
    pawn_location[1] = int(pawn_location[1])

    rows_traveled = abs(pawn_location[0] - bishop_location[0])

    # LOGIC
    if bishop_location[1] + (1 * rows_traveled) == pawn_location[1]:
        print("True")
    elif bishop_location[1] - (1 * rows_traveled) == pawn_location[1]:
        print("True")
    else:
        print("False")

    t_cases -= 1
