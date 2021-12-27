def getBlocks(grid, pair):
    blockSize = 1
    maS = [pair]
    seen = set()
    seen.add(pair)
    while maS:
        x, y = maS.pop(0)
        if not grid[x][y]:
            return
        for dx in [-1, 1]:
            if (x + dx, y) not in seen:
                if 0 <= (x + dx) < 4:
                    if grid[x + dx][y] == grid[x][y]:
                        blockSize += 1
                        maS.append((x + dx, y))
                        seen.add((x + dx, y))
        for dy in [-1, 1]:
            if (x, y + dy) not in seen:
                if 0 <= (y + dy) < 4:
                    if grid[x][y + dy] == grid[x][y]:
                        blockSize += 1
                        maS.append((x, y + dy))
                        seen.add((x, y + dy))

    return seen, blockSize


def makeNext(grid):
    next = []
    blocks = []
    for i in range(0, 4):
        col = []
        for j in range(3, -1, -1):
            col.append(board[j][i])
        next.append(col)
    return next


def gravity(grid, next, nextPos):
    for i in range(0, 4):
        for k in range(0, 4):
            for j in range(3, 0, -1):
                if not grid[j][i]:
                    nextRow = j - 1
                    grid[j][i] = grid[nextRow][i]
                    grid[nextRow][i] = False
    for i in range(0, 4):
        for k in range(3, -1, -1):
            if not grid[k][i]:
                grid[k][i] = next[i][nextPos[i]]
                nextPos[i] = (nextPos[i] + 1) % 4
    return grid, nextPos


def clearBlocks(grid):
    sizes = []
    for i in range(0, 4):
        for j in range(0, 4):
            if grid[i][j]:
                seen, size = getBlocks(grid, (i, j))
                if size > 1:
                    for xy in seen:
                        x, y = xy[0], xy[1]
                        grid[x][y] = False
                    sizes.append(size)
    if sizes:
        score = 1
        for size in sizes:
            score *= size
        return grid, score


grid = []
board = []
for i in range(0, 4):
    board.append(input("Row" + str(i + 1)))
for row in board:
    rowDict = {}
    for i in range(0, 4):
        rowDict[i] = row[i]
    grid.append(rowDict)
nextO = makeNext(grid)
nextStatus = [0, 0, 0, 0]
score = 0
rounds = 123
while rounds != 123123:
    grid2 = grid.copy()
    rounds = int(input("Rounds"))
    for i in range(0, rounds):
        grid2, curScore = clearBlocks(grid2)
        score += curScore
        if score == 0:
            print("GAME OVER")
            exit()
        grid2, nextStatus = gravity(grid2, nextO, nextStatus)

    for row in grid2:
        print("".join([row[i] for i in range(0, 4)]))
    print(score)
