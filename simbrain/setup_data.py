from __future__ import print_function
import numpy as np


def main(N_obs):

    vocab = np.identity(5, dtype=int)

    T = np.zeros((5, 5))

    # create transition matrix; the network should approximate each of these
    T[0, [1, 2, 3, 4]] = [.5, .2, .1, .2]
    T[1, [2, 4]]       = [.7, .3]
    T[2, [0, 1, 2, 3]] = [.1, .2, .3, .4]
    T[3, :]            = [.6, .1, .1, .1, .1]
    T[4, [1, 3]]       = [.4, .6]

    # create input and output data
    I = np.array(
        [list(vocab[i]) for i in range(5) for j in range(N_obs)],
        dtype=int
    )

    O = np.ndarray(I.shape, dtype=int)

    r5 = list(range(5))  # to be re-used in loops
    for i in r5:
        # ith row of transition matrix are transition probabilities
        transition_probabilities = T[i]

        for j in range(N_obs):
            O[N_obs*i + j] = vocab[
                np.random.choice(r5, p=transition_probabilities)
            ]

    np.savetxt('input.csv', I, fmt='%i', delimiter=',')
    np.savetxt('output.csv', O, fmt='%i', delimiter=',')
    np.savetxt('transition.csv', T, fmt='%1.2f', delimiter=',')


if __name__ == '__main__':
    help_msg = \
'''
Usage:
    python setup_data.py <number-of-obs-per-word>
'''
    import sys
    try:
        N_obs = int(sys.argv[1])
        main(N_obs)

    except Exception as e:
        print('got exception: {}\n'.format(e))
        print(help_msg)
