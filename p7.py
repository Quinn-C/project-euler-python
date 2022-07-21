#!/usr/bin/env python3

import freq_used_func

''' Create a infinite sequence object to yield from 0 '''
num_generator = freq_used_func.infinite_sequence()

count = 0
''' Keep generate numbers, until while loop exit '''
for num in num_generator:
    if (num == 0 or num == 1):
        continue
    if (freq_used_func.isPrime(num)):
            count += 1
            if (count >= 10001):
                break
print(num)



