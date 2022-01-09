combMemo = {}


def combs(l, m, f, c):  # digits left, max repeats, current amount in a row, current character
    if f == m:
        return 0
    if l == 0:
        return 1
    if (l,m,f) in combMemo.keys():
        return combMemo[(l,m,f)]
    score = 0
    for let in letters:
        if let == c:
            score += combs(l - 1, m, f + 1, let)
        else:
            score += combs(l - 1, m, 1, let)
    combMemo[(l,m,f)] = score
    return score


def build(n, pLength, curChar, repeats, maxRepeats):
    if pLength == 0:
        return ""
    for char in letters:
        if char == curChar:
            ways = combs(pLength - 1, maxRepeats,repeats + 1, char)
            if ways >= n:
                return char + build(n, pLength - 1, char, repeats + 1, maxRepeats)
            n -= ways
        else:
            ways = combs(pLength - 1,maxRepeats,1,char)
            if ways >= n:
                return char + build(n,pLength - 1,char,1,maxRepeats)
            n -= ways

while True:
    upTo, maxRepeat, pLength = [int(x) for x in input().split()]
    maxRepeat += 1
    n = int(input())
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = alpha[:upTo]
    print(build(n,pLength,0,"",maxRepeat))