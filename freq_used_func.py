#!/usr/bin/env python3

'''
Frequently used functions
'''
import math

def isPrime(num):
    ''' Check if a number is a prime number, return boolean'''
    flag = False
    for i in range(2, int(math.sqrt(num) + 1)):
        if (num % i == 0):
            flag = True
            break
    if flag:
        return False
    else:
        return True

def num_generator(num):
    ''' Generate numbers from num to 1, yield each of them '''
    while num > 0:
        yield num
        num -= 1


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
