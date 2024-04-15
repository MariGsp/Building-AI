"""
New social media follower: John37330190
Use Bayes rule to calculate the probability of the new follower being a bot.
Probabilities are in decimal form.
"""


def bot8(pbot, p8_bot, p8_human):
    """Gets and prints  the probability of the new follower being a bot

        Parameters
        ----------
        pbot : float
            The probability that a new follower is a bot
        p8_bot : float
            The probability that the username of a bot account includes an 8-digit number
        p8_human : float
            The probability that the username of a human account includes an 8-digit number
        Returns
        -------
        float
            The probability of the new follower being a bot
        """
    p8 = p8_bot * pbot + p8_human * (
            1 - pbot)  # Formula: P(8-digits) = P(8-digits|bot) x P(bot) + P(8-digits|human) x P(human)
    pbot_8 = p8_bot * pbot / p8  # Formula: P(bot|8-digits) =  P(8-digits|bot) x P(bot) / P(8-digits).
    print(pbot_8)


# you can change these values to test your program with different values
pbot = 0.1
p8_bot = 0.8
p8_human = 0.05

bot8(pbot, p8_bot, p8_human)
