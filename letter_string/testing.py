import numpy as np
from copy import deepcopy
import random
import json
import argparse

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

parser = argparse.ArgumentParser()
parser.add_argument('--num_permuted', help="give a number of letters in the alphabet to permute from 2 to 26", type=int)
args = parser.parse_args()

def k_derange(k=2, letters=letters):
    if k == 1:
        return letters
    
    to_shuffle = sorted(random.sample(range(len(letters)), k=k))
    shuffled = random.sample(to_shuffle, k=len(to_shuffle))
    not_derangement = sum([i == shuffled[to_shuffle.index(i)] for i in to_shuffle])

    while not_derangement:
        shuffled = random.sample(to_shuffle, k=len(to_shuffle))
        not_derangement = sum([i == shuffled[to_shuffle.index(i)] for i in to_shuffle])
    shuffled_letters = [letters[i] if i not in to_shuffle else letters[shuffled[to_shuffle.index(i)]] for i in range(len(letters))]
    return shuffled, shuffled_letters

sl = k_derange(k = args.num_permuted)
    
print(sl)

