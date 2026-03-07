def factorial (n):
    result=1

    if n<0:
        return False
    elif n==0 or n==1:
        return 1
    else:
        for i in range(1,n+1):
            result*=i

        return result
    
print(factorial(5))

    
