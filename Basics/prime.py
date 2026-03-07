import math

def prime(num):

    if num <1:
        return False
    
    for i in range (2, int(math.sqrt(num)+1)):
        if num % i ==0:
            return False
    return True

print(prime(18))
