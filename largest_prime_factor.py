n=int(input('enter the number to find prime factors of : '))

def prime_no(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
                break
            
        else:
            return True

def prime_factor(n):
    factor=[]
    for j in range(2,n+1):
        if n%j==0:
            if prime_no(j):
                factor.append(j)
    return factor


print(prime_factor(n))