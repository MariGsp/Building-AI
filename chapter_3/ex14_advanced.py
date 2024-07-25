import numpy as np
from io import StringIO

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''


def main():
    np.set_printoptions(precision=1)  # this just changes the output settings for easier reading

    # read in the training data and separate it to x_train and y_train
    x_train = []
    y_train = []
    lines = train_string.split('\n')
    for line in lines:
        if line:
            values = line.split()
            x_train.append(values[0:-1])
            y_train.append(values[-1])

    # convert lists to numpy arrays
    x_train = np.asarray(x_train, dtype=np.float32)
    y_train = np.asarray(y_train, dtype=np.float32)

    # fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_train, y_train)[0]

    # read in the test data and separate x_test from it
    x_test = []
    y_test = []
    lines = test_string.split('\n')
    for line in lines:
        if line:
            values = line.split()
            x_test.append(values[0:-1])
            y_test.append(values[-1])

    # convert lists to numpy arrays
    x_test = np.asarray(x_test, dtype=np.float32)
    y_test = np.asarray(y_test, dtype=np.float32)

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prices for the two new cabins in the test data set
    print(x_test @ c)


main()
