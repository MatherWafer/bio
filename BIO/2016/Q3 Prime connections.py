l, p, q = map(int, input().split(" "))
from math import log2
from collections import deque

def primes(max):
    a = [True] * max
    a[0] = a[1] = False
    for num, prime in enumerate(a):
        if prime:
            yield num
            for f in range(num ** 2, max, num):
                a[f] = False
    return a

seen = []
queue = deque()
primes = list(primes(l))

def bfs(cur, target):
    queue.append((cur, 1))
    primes.remove(cur)
    while queue:
        node, steps = queue.popleft()
        if node == target:
            return steps
        if node not in seen:
            #print("Ff")
            seen.append(node)
            for i in range(0,int(log2(q))+1):
                dif = 1 << i
                next_n = node + dif
                if next_n in primes:
                    #print("Adding {} to {}".format(dif,node))
                    primes.remove(next_n)
                    queue.append((next_n,steps+1))
                next_n = node - dif
                if node - dif in primes:
                    queue.append((next_n,steps+1))
                    primes.remove(next_n)
        else:
            print("Node seen")
print(bfs(p,q))