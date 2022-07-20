'''Plan
1. calculate terms in fibonacci sequence
    cal fib by using recursion
    create a dict for storing calculated fibs
    base case if n = 1, return 1
    check if fib(n) in the dict
        if yes, return dict(n)
        else cal fib(n-1)+fib(n-2)
            store it in the dict
2. check if the term less than 4 million and it is even
3. if yes, add it to the sum
'''
# n starts from 2, 3
# fib(n) starts from 1, 2
def fib(n):
    memo = {}
    if n < 0:
        raise IndexError('n cannot be negative!')
    elif n == 0 or n == 1:
        return n
    
    if n in memo:
        return memo[n]
    
    result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    
    return result

def even_fibonacci(max):
    n, sum = 2, 0
    while fib(n) < max:
        if fib(n) % 2 == 0:
            sum += fib(n)
        n += 1
    
    print(sum)
    
#fib(7)   
even_fibonacci(4000000)