"""Write a program that counts the number of occurrences of "11"
in an input sequence of zeros and ones.
The input of the program is just the sequence, and
it should return a single number,
which is the number of occurrences of "11"."""


def count11(seq):
    count = 0
    for item in range(0, len(seq) - 1):
        if seq[item] == 1 and seq[item + 1] == 1:
            count += 1
    return count


print(count11([0, 0, 1, 1, 1, 0]))  # this should print 2
