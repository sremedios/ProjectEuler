from math import sqrt

def sumSquareDif(top):
    
    
    sumSq = sum([x**2 for x in range(1, top+1)])
    sqSum = sum([x for x in range(1, top+1)])**2
    return sqSum - sumSq

n = int(input())

print (sumSquareDif(n))
