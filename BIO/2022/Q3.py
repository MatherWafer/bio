arrange,j = input().split()
j = int(j)
nArrange = [ord(x) - ord('a')  for x in arrange]
spaces = {}
spaces[0] = [True for i in range(len(arrange))]

def product(aList):
    prod = 1
    for num in aList:
        prod = prod * num
    return prod


for i in range(1,len(arrange)):
    prev = spaces[i-1].copy()
    letIndex = nArrange.index(i-1)
    spaces[i] = prev
    spaces[i][letIndex] = False

def getWays(num):
    nums = []
    cIndex = nArrange.index(num)
    nums.append(cIndex)
    cIndex -=1
    while cIndex >= 0 and not spaces[num][cIndex]:
        nums.append(cIndex)
        cIndex -=1
    return sorted(nums)

ways = {}
nWays = [0 for i in range(len(arrange))]
for num in range(len(arrange)):
    curWays = getWays(num)
    ways[num] = curWays
    nWays[num] = len(curWays)


def build(n,slot):
    if n == 0:
        return ""
    for option in ways[slot]:
        if slot == len(arrange) - 1:
            combs = 1
            n -= combs
            if combs > n:
                return str(option) + build(n,slot+1)
        else:
            combs = product(nWays[slot+1:])
            if combs >= n:
                return str(option) + build(n,slot+1)
            n-= combs
#print(ways)
#print(nWays)
ans = build(j,0)
print("".join([chr(ord('A') + int(x)) for x in ans]))