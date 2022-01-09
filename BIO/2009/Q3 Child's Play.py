waysMemo = {}
import time

def ways(s):
    if s in waysMemo.keys():
        return waysMemo[s]
    if s == 0:
        return 1
    result = sum([ways(s - i) for i in range(1, 10) if s - i >= 0])
    waysMemo[s] = result
    return result


#print(ways(s), "Ways of making", s)
#print("Finished in ", (time.time() - start))


def build(s, n):
    if s == 0:
        return ""
    for i in range(1, 10):
        if s - i >= 0:
            combs = ways(s - i)
            if combs >= n:
                #print("Added ", i)
                return str(i) + build(s - i, n)
            n -= combs

while True:
    s, n = [int(x) for x in input().split()]
    start = time.time()
    ans = " ".join([x for x in build(s, n)])
    print(ans)
    print(time.time()-start)