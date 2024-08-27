# recursive is very abstract so I am going to do iterative now
# I will try to use ChatGPT as little as possible

import string
import time

target = "cat"
letters = list(string.ascii_lowercase)
max_len = 6

for l in range(1, max_len + 1):
    indices = [0] * l

    