from math import comb

n = int(input())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def makePass(length,n,ans =""):
    if length == 0:
        return ans
    start = (alpha.index(ans[-1])+ 1) if ans else 0
    for letter in range(start,36):
        can = comb(36 - (letter +1),length - 1)
        if can >= n:
            return makePass(length-1,n,ans + alpha[letter])
        n -= can

targ = 1
while comb(36,targ) < n:
    n = comb(36,targ)
    targ += 1

print(makePass(targ,n))