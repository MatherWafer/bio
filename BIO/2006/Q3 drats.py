s,d = [int(x) for x in input().split()]
max = 20 if s >= 20 else s
"""
table = [[0]*d] * s
table[0] = [1] + [0] * (d-1)
for i in range(0,s):
    for j in range(0,d-1):
        for k in range(1,max+1):
            if i + k < s - 2:
                table[i+k][j+1] += table [i][j]
print(table)
"""

memo = {}


def darts(s,d,first = True):
    if (s,d) in memo.keys():
        return memo[(s,d)]
    if s < 0:
        return 0
    if s == 0 and d == 0:
        return 1
    elif s == 0 and d > 0:
        return 0
    elif d == 0:
        return 0
    if first:
        return sum([darts(s-i*2,d-1,False) for i in range(1,max+1)],)
    else:
        v = sum([darts(s-i,d-1,False) for i in range(1,max+1)])
        memo[(s,d)] = v
        return v
print(darts(s,d))