#!/usr/bin/env python3

'''
Plan:
1. Use infinite number generator to yield number from one to two million
2. Use isPrime function to check the number it received is a prime number
    if yes, add it to the sum
    if not, skip

'''

import freq_used_func

primes_sum = 0
''' Create an inifinite number generator object '''
number_generator = freq_used_func.num_generator(2000000)

''' Loop through each number filter out the primes and get the sum and return it '''
for num in number_generator:
    if (num == 0 or num == 1):
        continue
    if (freq_used_func.isPrime(num)):
        primes_sum += num
print(primes_sum)



