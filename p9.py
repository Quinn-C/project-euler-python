#!/usr/bin/env python3

'''
Plan:
1. Based on the conditions get the relationship:
    1000 * (a + b) - 5 * (10 ** 5) = ab
    2 * b < 1000 - a

2. Double for loop:

'''
import time

start_time = time.time()

def find_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a, 1000):
            if (2 * b < 1000 - a):
                if ( 1000 * (a + b) - 5 * (10 ** 5) == a * b):
                    print(a * b * (1000 - a - b))
                    return True

find_pythagorean_triplet()


end_time = time.time()

print(end_time - start_time)
