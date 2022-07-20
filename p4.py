#!/usr/bin/env python3

'''
Question: two 3-digit numbers -> largest palindrome

Plan: use two 3 digit numbers from 999, decrement every single time

until you find a palindrome

How to check if a number is a palidrome
'''

def check_palidrome(number):
    string = str(number)
    l = len(string)

    for i in range(l):
        if(string[i] != string[l - 1 - i]):
            return False

    return True

def find_two_number(number_of_digit):
    start = 10 ** number_of_digit - 1
    print(start)
    end = 9 * (10 ** (number_of_digit - 1))
    max_multi = 0
    max_1 = 0
    max_2 = 0

    for i in range(start, end, -1):
        for j in range(start, end, -1):
            multi = i * j
            if check_palidrome(multi):
                if (multi > max_multi):
                    max_multi = multi
                    max_1 = i
                    max_2 = j
    print(max_multi, max_1, max_2)

