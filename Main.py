from QLearning import QLearning


if __name__ == '__main__':
    QL = QLearning("Examples/12.10")
    Q = QL.train(GAMMA = 0.9, ALPHA = 0.1, epochs = 1000)
    QL.test(Q)
