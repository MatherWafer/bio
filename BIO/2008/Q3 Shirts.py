from collections import deque


def shiftLeft(rack):
    left = rack.pop(0)
    rack.insert(3,left)
    return rack


def shiftRight(rack):
    right = rack.pop(6)
    rack.insert(3,right)
    return rack


def placeLeft(rack):
    mid = rack.pop(3)
    rack.insert(0,mid)
    return rack


def placeRight(rack):
    mid = rack.pop(3)
    rack.append(mid)
    return rack


def bfs(target,root):
    queue = deque()
    seen = set()
    queue.append((root,0))
    while queue:
        rack,steps = queue.popleft()
        if rack == target:
            return steps
        else:
            if tuple(rack) not in seen:
                seen.add(tuple(rack))
                rack1 = shiftLeft(rack[:])
                rack2 = shiftRight(rack[:])
                rack3 = placeLeft(rack[:])
                rack4 = placeRight(rack[:])
                for nShirts in [rack1,rack2,rack3,rack4]:
                    if tuple(nShirts) not in seen:
                        queue.append((nShirts,steps+1))
    print(seen)
shirts = [x for x in "1234567"]


print(bfs(shirts, [x for x in input()]))



