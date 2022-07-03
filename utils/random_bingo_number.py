import random

def generate_bingo_numbers():
    bingo = []

    b_column = random.sample(range(1, 16), 5)

    i_column = random.sample(range(16, 31), 5)

    n_column = random.sample(range(31, 46), 5)

    n_column[2] = 0

    g_column = random.sample(range(46, 61), 5)

    o_column = random.sample(range(61, 75), 5)

    bingo.extend([b_column, i_column, n_column, g_column, o_column])

    return bingo




