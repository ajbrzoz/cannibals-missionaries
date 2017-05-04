#! python3

"""
Program solving the missionaries and cannibals riddle (see description below) by printing out 
subsequent configurations of cannibals and missionaries on both river banks and in the boat.

Missionaries and cannibal riddle:
Three missionaries and three cannibals come to a river and find a boat that holds two people. 
Everyone must get across the river to continue on the journey. However, if the cannibals ever 
outnumber the missionaries on either bank, the missionaries will be eaten. Find a series of 
crossings that will get everyone safely to the other side of the river.

"""

# initial configuration (3 missionaries and cannibals on bank 1)
bank1 = {'c': 3, 'm': 3}
bank2 = {'c': 0, 'm': 0}
boat = {'c': 0, 'm': 0}


def print_state(dct1, dct2, dct3):
    """
    Prints each configuration in easily readable form
    """

    msg = """
    Bank 1: {} cannibal(s), {} missionary/ies
    Bank 2: {} cannibal(s), {} missionary/ies
    Boat: {} cannibal(s), {} missionary/ies
    """

    print(msg.format(dct1['c'], dct1['m'], dct2['c'], dct2['m'],
                     dct3['c'], dct3['m']))


def cann_miss(b1=bank1, b2=bank2, bo=boat):
    if all(x == 0 for x in b2.values()):  # bank2 is empty
        print_state(b1, b2, bo)
        b1['c'] -= 1  # 1 cannibal leaves bank1 and ...
        bo['c'] += 1  # ... goes on board

    b1['m'] -= 1  # 1 missionary leaves bank1 and ...
    bo['m'] += 1  # ... goes on board
    print_state(b1, b2, bo)

    if all(x == 0 for x in b1.values()):  # bank1 is empty
        bo['c'], bo['m'] = 0, 0  # 1 cannibal and 1 missionary go out of boat
        b2['c'] += 1  # 1 cannibal steps out on bank2
        b2['m'] += 1  # 1 missionary steps out on bank2
        print_state(b1, b2, bo)
        return  # final condition is met

    bo['m'] -= 1  # 1 missionary goes out of boat and ...
    b2['m'] += 1  # ... steps out on bank2
    print_state(b1, b2, bo)

    b1['c'] -= 1  # 1 cannibal leaves bank1 and ...
    bo['c'] += 1  # ... goes on board
    print_state(b1, b2, bo)

    bo['c'] -= 1  # 1 cannibal goes out of boat and ...
    b2['c'] += 1  # ... steps out on bank2
    print_state(b1, b2, bo)

    cann_miss(b1, b2, bo)  # another series of crossings


def main():
    cann_miss()


if __name__ == '__main__':
    main()
