# check palindrom works ezpz
# need to fix largestPalin to calculate products
# probably need O(n^2) alg to sweep through combinations of 999 998, 999 997, etc, 998, 998, 998, 997, etc

def checkPalindrome(n):
    nStr = str(n)

    for x in range(len(nStr)//2):
        if nStr[x] != nStr[-1-x]:
            return False
    return True

def largestPalin(digits):
    end = 10**(digits)
    start = 10**(digits-1)

    largest = 0
    for x in range(start, end):
        for y in range(start, end):
            if checkPalindrome(x*y) and x*y > largest:
                largest = x*y
    return largest


x = int(input("Enter digits: "))

print(largestPalin(x))
