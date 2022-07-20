#!/usr/bin/env python3
'''
Plan:
1. Find all unique prime factors that number from 1-10 needed.
2. Check how many of each prime factors needed for making itself to the power of the quantity less or
   equal to 10.
3. Calculate the multiplication of all exponentiation that we calculated above.

'''
def isPrime(num):
    ''' Check if a number is a prime number, return boolean'''
    flag = False
    for i in range(2, num):
        if (num % i == 0):
            flag = True
            break
    if flag:
        return False
    else:
        return True

def num_generator(maximum):
    ''' Generate numbers consistently return a generator object '''
    cur = maximum
    while cur > 0:
        yield cur
        cur = cur - 1

''' Create a set to store all prime factors '''
prime_factor_set = set()
print(prime_factor_set)

''' Get all prime factors for numbers from 1 to 20, store in the set '''
for num in num_generator(20):
    f = 2
    while ( f <= num):
        if (num % f != 0):
            if (isPrime(f) and f not in prime_factor_set):
                prime_factor_set.add(f)
        f += 1

print(prime_factor_set)

''' Create a dictionary to store all prime_factors and its times '''
prime_factor_dict = {}
for pf in prime_factor_set:
    print(pf)
    i = 1
    while (pf ** i < 20):
        i = i + 1
    prime_factor_dict[pf] = i - 1
print(prime_factor_dict)

''' Each key to the power of its value, and calcuate the multiplication of all exponentiations '''
def cal_multiplication(prime_factor_dict):
    sum_multiplication = 1
    for key, value in prime_factor_dict.items():
        sum_multiplication *= (key ** value)

    print(sum_multiplication)



