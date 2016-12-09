from math import sqrt, ceil

def isPrime(n):
    end = ceil(sqrt(n))
    for i in range(2, end):
        if n%i == 0:
            return False
    return True

def primeFactors(n):
    factors = []
    end = ceil(sqrt(n))
    for i in range(2, end):
        if isPrime(i) and n%i == 0:
            factors.append(i)
    return factors

n = int(input("enter\n"))
print(primeFactors(n))
