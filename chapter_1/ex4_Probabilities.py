import random


def main():
    x = random.random()

    if x < 0.80:
        favourite = "dogs"
    elif x < 0.90:
        favourite = "cats"
    else:
        favourite = "bats"

    print("I love " + favourite)


main()
