a,b,c,d,n = [int(x)for x in input("a b c d n").split()]
letters = ["A","B","C","D"]
from math import factorial
def perm(a,b,c,d):
    return factorial(a+b+c+d) //(factorial(a) * factorial(b) * factorial(c) * factorial(d))


def solve(a,b,c,d,n):
    if a + b + c + d == 0:
        return ""
    if a > 0:
        if perm(a-1,b,c,d) >= n:
            return "A" + solve(a-1,b,c,d,n)
        n -= perm(a-1,b,c,d)
    if b > 0:
        if perm(a,b-1,c,d) >= n:
            return "B" + solve(a,b-1,c,d,n)
        n -= perm(a,b-1,c,d)
    if c > 0:
        if perm(a,b,c-1,d) >= n:
            return "C" + solve(a,b,c-1,d,n)
        n -= perm(a,b,c-1,d)

    return "D" + solve(a,b,c,d-1,n)


print(solve(a,b,c,d,n))
