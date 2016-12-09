def smallestMult(n):
    prod = 1

    for x in range (1, n+1):
        prevProd = prod
        while prod%x != 0:
            prod += prevProd

    return prod

n = int(input())

print(smallestMult(n))

