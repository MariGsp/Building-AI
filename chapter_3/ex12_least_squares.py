import numpy as np

X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])  # actual price
c = np.array([3000, 200, -50, 5000, 100])  # coefficient values


def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        # calculate the predicted price
        pred_price = (xi @ c)
        # subtract it from the actual price yi
        difference = yi - pred_price
        # square the difference
        squared_difference = difference ** 2
        # add up all the differences
        sse = sse + squared_difference
        pass

    print(sse)


squared_error(X, y, c)
