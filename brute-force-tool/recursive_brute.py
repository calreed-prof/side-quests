# This file will aim to test my knowledge on brute forcing techniques
# This uses recursion and took my way too long to figure out

import string
import time

target = "cat"
letters = list(string.ascii_lowercase)
max_len = 6


def brute_force(cur_guess, target, letters, max_len):
    if cur_guess == target:
        print(f"Nailed it my guy, Password is {cur_guess}")
        return True
    
    if len(cur_guess) == max_len:
        return False
    
    for letter in letters:
        if brute_force(cur_guess + letter, target, letters, max_len):
            return True
        
start_time = time.time()

brute_force('', target, letters, max_len)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"{elapsed_time:.4f} seconds")
