from collections import defaultdict,deque
#FULL MARKS
def row():
    row = defaultdict(int)
    for i in range(0,5):
        row[i] = 0
    return row


def getYX(pos):
    return divmod(pos-1,5)


board = defaultdict(row)


p,s,n = [int(x) for x in input().split()]
sequence = [int(x) for x in input().split()]
curStep = 0
y,x = getYX(p)
queue = deque()
for i in range(n):
    queue.append((y,x))
    while queue:
        y,x = queue.popleft()
        board[y][x] += 1
        if board[y][x] == 4:
            board[y][x] -= 4
            for pair in [(y-1,x),(y,x-1),(y+1,x),(y,x+1)]:
                queue.append(pair)
    p += sequence[curStep]
    if p > 25:
        p -= 25
    curStep += 1
    curStep %= len(sequence)
    y,x = getYX(p)

for i in range(5):
    row = []
    for j in range(0,5):
        row.append(str((board[i][j])))
    print(" ".join(row))

