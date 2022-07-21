#!/usr/bin/env python3

'''
Plan:
1. Covert 1000-digit to a string, yield each digit
2. For loop: loop through the whole string by moving two pointers, [i, i + numstr]
    1) Store the elements between and including these two pointers into a set
    2) Check if there is 0 in this set,
        if yes, skip to next iteration
        if no, calculate the product of numbers from i to i + number
3. Function: calculate the product
'''
long_number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

long_str = str(long_number)

str_len = 13
max_product = 0
short_num_set = set()
def cal_product(short_num_str):
    ''' Calculate the product of all numbers in the list, return the product '''
    product = 1
    for i in range(len(short_num_str)):
        product *= int(short_num_str[i])
    print("The current product is: ", product)
    return product

''' Loop through all characters in the str_number '''
for i in range(len(long_str) - str_len):
    ''' Check if the characters inside and contain two pointers has '0' '''
    for j in range(i, i + str_len):
        short_num_set.add(int(long_str[j]))

    ''' If '0' exist in the set, clear the set and skip to the next iteration '''
    if 0 in short_num_set:
        short_num_set.clear()
        continue
    else:
        ''' Calcuate the product '''
        product = cal_product(long_str[i: str_len + i])

    ''' Assign the larger product in each iteration '''
    if product > max_product:
        max_product = product

print("The max product is:", max_product)
