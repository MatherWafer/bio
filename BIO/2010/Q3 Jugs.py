
j,n = [int(x) for x in input().split()]
capacs = [int(x) for x in input().split()]
jugs = [0] * len(capacs)


from collections import deque
from itertools import permutations

pours = permutations(list(range(0, len(jugs))), 2)


def pour(jugs, jugA, jugB):  # jugB poured into jugA
    A = jugs[jugA]
    B = jugs[jugB]
    dif = capacs[jugA] - A
    if dif >= B:
        jugs[jugA] += B
        jugs[jugB] = 0
    else:
        jugs[jugA] += dif
        jugs[jugB] -= dif
    return jugs


def fill(jugs, i):
    jugs[i] = capacs[i]
    return jugs


def empty(jugs, i):
    jugs[i] = 0
    return jugs


def bfs(target, jugs):
    seen = []
    queue = deque()
    queue.append((jugs,0))
    while queue:
        pours = permutations(list(range(0, len(jugs))), 2)
        curJugs, steps = queue.popleft()
        print(curJugs,steps)
        seen.append(tuple(curJugs))
        if target in curJugs:
            return steps
        for way in pours:
            #print("Entered pour")
            a, b = way
            pJugs = pour(curJugs[:],a,b)
            if tuple(pJugs) not in seen and pJugs not in queue:
                queue.append((pJugs, steps + 1))
        for i in range(len(curJugs)):
            if curJugs[i] < capacs[i]:
                fJugs = fill(curJugs[:],i)
                if tuple(fJugs) not in seen and fJugs not in queue:
                    queue.append((fJugs, steps+1))
            if curJugs[i] > 0:
                eJugs = empty(curJugs[:],i)
                if tuple(eJugs) not in seen and eJugs not in queue:
                    queue.append((eJugs,steps + 1))

print(bfs(n,jugs))