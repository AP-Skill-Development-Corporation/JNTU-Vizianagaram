def sqrt(n):
    return n**(0.5)

def factors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
            
def factorial(f):
    if f==0 or f==1:
        return 1
    else:
        return f*factorial(f-1)
    
def is_palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
    
def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "Odd"
    