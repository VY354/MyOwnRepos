from math import *
import numpy as np


def main():
    actFunc = lambda x: x

    inn = 1  # input layer neurons number
    onn = 1  # output layer neurons number

    # hidden layers structure: array of type [ [ln1 , nn1], [... , ...], ... ],
    # where ln -> layers number, nn -> neurpns number in this layers
    hlstruct = [[5, 3]]

    il = np.ones(inn)  # input layer
    ol = np.ones(onn)  # output layer
    hls = [np.ones((dim[0], dim[1])) for dim in hlstruct]  # hidden layers
    biases = [1 for i in range(np.sum([x[0] for x in hlstruct]))]  # biases

    fls = [[1, inn]] + hlstruct + [[1, onn]]  # full layers structure (include il and ol)

    layers = []  # list of all layers, made corresponding to with full layers structure
    layers.append(il)
    for lg in hls:
        for l in lg:
            layers.append(l)
    layers = [np.array(l) for l in layers]
    layers.append(ol)

    weights = []
    for i in range(len(fls) - 1):
        weights.append(np.ones((fls[i + 1][1], fls[i][1])))
        for j in range(fls[i + 1][0] - 1):
            weights.append(np.ones((fls[i + 1][1], fls[i + 1][1])))

    propagate(np.ones(inn), layers, weights, biases, actFunc)


def propagate(input, layers, weights, biases, actFunc):
    layers[0] = input

    # forward propagation
    # for each layers from second:
    # for current layer generate list of neurons values as:
    # for each row in current weights matrix, get dot prod. of
    # prev. layer neurons values with this row plus bias and pass it to activation function
    # as a result -> get current layer neurons values
    for i in range(1, len(layers)):
        layers[i] = np.array(
            [actFunc(np.dot(layers[i - 1], w) + (biases[i - 1] if i < len(layers) - 1 else 0)) for w in weights[i - 1]])

    for l in layers:
        print(l)


if __name__ == '__main__':
    main()
