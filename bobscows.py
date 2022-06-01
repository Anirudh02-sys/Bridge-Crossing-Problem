from Crossing import Crossing_Bridge


def main():
    n = int(input("Enter the number of cows that are to be moved from A to B : "))
    cows = input("Enter the speed of {} cows (in minutes) : ".format(n))
    cows = list(map(int, cows.split()))
    cross = Crossing_Bridge(cows)
    cross.show_crossing()


main()
