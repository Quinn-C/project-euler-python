'''
prime numbers are numbers can only divided by 1 and itself.
prime factors are the prime numbers can be multiplied to give the original number.

Plan:
- start to use prime number 2 to divide the number
- divide the reminder by 2
   - if cannot, then use 3, ....itself
'''

def find_prime_factors(number):
    new_num = number
    largest_f = 1
    f = 2

    while (f * f <= new_num):
        if (new_num % f == 0):
            new_num = int(new_num / f)
            largest_f = f
            print(new_num, largest_f)
        else:
            f += 1

    if (new_num > largest_f):
        largest_f = new_num

    print(largest_f)
