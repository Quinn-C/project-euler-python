#!/usr/bin/env python3

'''
Plan:

1. Create a function to generate number as a generator object - num_generator
2. for loop: receive the number, square it, and sum all squares, return the sum - sum_squares
3. for loop: call the num_generator again, add sum all numbers, square the sum - square_sum
4. calcuate the diff between the result from square_sum and sum_squares - diff_sum_square
'''

def num_generator(num):
    ''' Generate numbers from num to 1, yield each of them '''
    while num > 0:
        yield num
        num -= 1

''' Create two num generator objects '''
num_generator_one = num_generator(100)
num_generator_two= num_generator(100)

sum_squares = 0
sum_num = 0
square_sum = 0
diff_sum_square = 0

''' square each nums, and add all squares and get the sum_squares'''
for num in num_generator_one:
    square_num = num ** 2
    sum_squares += square_num
print(sum_squares)

''' Sum all nums to get the sum_num '''
for num in num_generator_two:
    sum_num += num
print(sum_num)

''' Square the sum '''
square_num = sum_num ** 2
print(square_num)

''' Calculate the diff between square_num and sum_squares '''
diff_sum_square = square_num - sum_squares
print(diff_sum_square)





