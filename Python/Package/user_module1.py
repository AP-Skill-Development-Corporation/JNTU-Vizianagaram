def is_perfect(n):
    fc=0
    for i in range(1,n):
        if n%i==0:
            fc += i
    if fc==n:
        return True
    else:
        return False
    
def is_prime(x):
    for i in range(2,x//2):
        if x%i==0:
            return False
    return True