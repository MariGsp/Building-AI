"""
Print out conditional probabilities of each nationality given that the winner works in the fishing industry.
Formula:
Prob (country ∣ fisher) = fishers(country) / fishers(total)
"""


def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    # populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]
    total_fishers = sum(fishers)
    # total_population = sum(populations)

    prob = []

    for fisher_n in fishers:
        prob_fisher = (fisher_n / total_fishers) * 100
        prob.append(prob_fisher)

    for country, prob in zip(countries, prob):
        print("%s %.2f%%" % (country, prob))


main()
