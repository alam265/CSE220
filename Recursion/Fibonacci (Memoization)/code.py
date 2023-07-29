import numpy as np
F= np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])


def fib(n):
    if n == 0 or n == 1:
        F[n] = n 
        return n 
    else:
        if F[n-2] == -1 and F[n-1] == -1 :
            F[n-2] =  fib(n-2)
            F[n-1] = fib(n-1)

        return F[n-2] + F[n-1] 
    
print(fib(10))