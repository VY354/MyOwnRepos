from math import *
import numpy as np

from dataclasses import dataclass, field, fields, asdict, astuple

@dataclass
class ANN:
    inputNeuronsNumber: int = field(default=0, init=True)
    outputNeuronsNumber: int = field(default=0, init=True)
    hiddenLayersStructure: list = field(default_factory=list, init=True)
    __fullLayersStructure: list = field(default_factory=list)

    __biases: list = field(default_factory=list, init=False)
    __weights: list = field(default_factory=list, init=False)
    __layers: list = field(default_factory=list, init=False)

    activationFunction: object = field(default=(lambda x: x), init=True)
    useBiases: bool = field(default=False, init=True)

    def initialize(self):
        # creating full layers structure (include input and output)
        self.__fullLayersStructure = [[1, self.inputNeuronsNumber]] + self.hiddenLayersStructure + [[1, self.outputNeuronsNumber]]

        # generate in and out layers and 1d array
        inputLayer = np.ones(self.inputNeuronsNumber)
        outputLayer = np.ones(self.outputNeuronsNumber)

        # generate layers array with corresponding layers structure (num of hidden layers and number of
        # neurons in each hidden layer)
        self.__layers = []
        self.__layers.append(inputLayer)
        for layerGroup in self.hiddenLayersStructure:
            for l in range(layerGroup[0]):
                self.__layers.append([np.ones(layerGroup[1])])
        self.__layers.append(outputLayer)
        self.__layers = [np.array(layer) for layer in self.__layers]

        # create weights matrices depending on layers structure
        self.__weights = []
        for i in range(len(self.__fullLayersStructure) - 1):
            self.__weights.append(np.ones((self.__fullLayersStructure[i + 1][1], self.__fullLayersStructure[i][1])))
            for j in range(self.__fullLayersStructure[i + 1][0] - 1):
                self.__weights.append(np.ones((self.__fullLayersStructure[i + 1][1], self.__fullLayersStructure[i + 1][1])))

        # create biases list if needed
        if self.useBiases:
            self.__biases = [1 for i in range(np.sum([x[0] for x in self.hiddenLayersStructure]))]

    # propagate input data
    def run(self, inputData: list):
        self.__layers[0] = inputData
        for i in range(1, len(self.__layers)):
            self.__layers[i] = np.array(
                [self.activationFunction(np.dot(self.__layers[i - 1], w) +
                                         (self.__biases[i - 1] if (self.__biases and i < len(self.__layers) - 1) else 0))
                 for w in self.__weights[i - 1]])

        for l in self.__layers:
            print(l)

    def __propagation(self):
        pass

    def __backPropagation(self):
        pass

    def learn(self):
        pass


def main():
    # input layer neurons number
    inn = 1
    # output layer neurons number
    onn = 1
    # hidden layers structure: array of type [ [ln1 , nn1], [... , ...], ... ],
    # where ln -> layers number, nn -> neurons number in this layers
    hlstruct = [[4, 3]]

    actFunc = lambda x: x

    ann = ANN(
        inputNeuronsNumber=inn,
        outputNeuronsNumber=onn,
        hiddenLayersStructure=hlstruct,
        useBiases=False,
        activationFunction=actFunc
    )

    ann.initialize()

    inputData = [1]
    ann.run(inputData)


if __name__ == '__main__':
    main()
