from QLearning import QLearning


if __name__ == '__main__':
    QL = QLearning("Examples/12.10_paths",beta = 5,paths_given = True)
    Q = QL.train(GAMMA = 1, ALPHA = 0.1, epochs = 1000,test = False)
    QL.solve(Q,print_policy = True)
