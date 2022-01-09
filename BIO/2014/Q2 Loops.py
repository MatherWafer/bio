faces = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


def getOpposite(face):
    if face == "up":
        return "down"
    elif face == "down":
        return "up"
    elif face == "left":
        return "right"
    elif face == "right":
        return "left"


class tile:
    def __init__(self,up,down,left,right):
        self.unSeen = {'R':True,'G':True}
        self.directions = {"up":up,"down":down,"left":left,"right":right}

    def match(self,direction):
        for f in self.directions:
            if self.directions[f] == self.directions[direction] and f != direction:
                return f
        pass


grid = []
tiles = {1:tile('R','R','G','G'), 2:tile('G','G','R','R'), 3:tile('R','G','R','G'),4:tile('R','G','G','R'),5:tile('G','R','G','R'),6:tile('G','R','R','G')}
print(tiles[2].match("down"))

n = int(input("N"))

nGrid = ["1341","5264","4235","4454"]

grid = []
for i in range(0,n):
    row = [tiles[int(f)] for f in input("Row").split(" ")]
    grid.append(row)
totals = []
for color in ['R','G']:
    print(color)
    total = 0
    loops = []
    for i in range(0,n):
        for j in range(0,n):
            count = 1
            print(grid[i][j].unSeen[color])
            if (i,j) not in loops:
                loop = [(i,j)]
                grid[i][j].unSeen[color] = False
                end,out = [f for f in grid[i][j].directions if grid[i][j].directions[f] == color]
                y,x = i,j
                dy,dx = faces[out]
                if 0 <= y + dy < n and 0 <= x + dx < n:
                    ny,nx = dy + y,dx + x
                    entry = getOpposite(out)
                    while (ny,nx) != (i,j) and grid[ny][nx].directions[entry] == color:
                        loop.append((ny,nx))
                        count += 1
                        print(count)
                        grid[ny][nx].unSeen[color] = False
                        out = grid[ny][nx].match(entry)
                        dy,dx = faces[out]
                        if 0 <= ny + dy < n and 0 <= nx + dx < n:
                            ny, nx = dy + ny, dx + nx
                        else:
                            break
                        entry = getOpposite(out)

                    if (ny,nx) == (i,j):
                        loops += loop
                        print("Found loop")
                        total += count

    print(total)
    totals.append(total)

print(totals[0],totals[1])




