# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

'''Plan: 
input: 3,5,1000
output: ?
for loop
    check if multi = i*3 less than 1000
        if yes, sum = sum + multi

'''

# def sum_of_multiples(a,b,c):
#     sum, sum1, sum2 = 0, 0, 0
#     for i in range(1, c):
#         multi = i*a
#         if multi < c:
#             sum1 = sum1 + multi
#         else:
#             break
            
#     for j in range(1, c):
#         multi2 = j*b
#         if multi2 < c:
#             sum2 = sum2 + multi2
#         else:
#             break
#     sum = sum1 + sum2
    
def sum_of_multiples(a, b, c):
    sum = 0
    for i in range(1, c):
        if i % a == 0 or i % b == 0:
            sum += i          
    print(sum)
    
sum_of_multiples(3, 5, 1000)
            