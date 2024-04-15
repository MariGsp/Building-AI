import numpy as np

countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26]


def guess(winner_gender):
    # global fishers_total

    guess = None
    biggest = 0.0

    if winner_gender == 'female':
        fishers = female_fishers
        fishers_total = np.sum(female_fishers)
    else:
        fishers = male_fishers
        fishers_total = np.sum(male_fishers)

    for f in range(len(fishers)):
        prob = (fishers[f] / fishers_total) * 100
        if prob > biggest:
            biggest = prob
            guess = countries[f]

    return (guess, biggest)


def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))


main()
