import sys
import math    

def next_prime(n):
    is_prime = False
    n += 1
    while not is_prime:
        if n !=2 and n % 2 == 0:
            n += 1
        else:
            j = math.ceil(math.sqrt(n))
            if j % 2 == 0:
                j -= 1
            is_prime = True
            k = 3
            while k <= j : 
                if n % k == 0:
                    is_prime = False
                    n += 1
                    break
                else:
                    k += 2
    return n
print(next_prime(int(input())))