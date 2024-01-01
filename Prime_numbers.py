import sys
import math

T = int(input())

for line in sys.stdin:
    i = int(line.strip())

    if i <= 1:
        print("Not prime")
    elif i !=2 and i % 2 == 0:
        print("Not prime")
    else:
        j = math.ceil(math.sqrt(i))
        if j % 2 == 0:
            j -=1
        is_prime = True
        k = 3
        while k <= j : 
            if i % k == 0:
                is_prime = False
                break
            else:
                k += 2
        if is_prime == True:
            print("Prime")
        else:
            print("Not prime")
      