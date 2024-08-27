# This file will aim to test my knowledge on brute forcing techniques

target = "p"
all_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

pass_guess = []

for key in all_keys:
    if key == target:
        print(f"target is {key}")