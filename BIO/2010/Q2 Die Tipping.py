vertStrip = [1, 2, 6, 5]
horizStrip = [1, 4, 6, 3]

faces = [(-1, 0), (0, 1), (1, 0), (0, -1)]
directions = ["up", "right", "down", "left"]
heading = 0


class dice:
    def __init__(self):
        self.y, self.x = 5, 5
        self.vert = [1, 5, 6, 2]  #top,towards,bottom,away
        self.horiz = [1, 4, 6, 3] #top,right,bottom,left
        self.heading = 0

    def top(self):
        return self.vert[0]

    def setHeading(self, newHeading):
        self.heading = newHeading

    def coords(self):
        return self.y, self.x

    def move(self, face):
        print("Moving", directions[faces.index(face)])
        if face[0] != 0:  # movement is regarding y, vertical face changed
            print(self.vert)
            dy = face[0]
            if dy == -1: #up
                cur = self.vert.pop(0)
                self.vert.append(cur)
            elif dy == 1: #down
                new = self.vert.pop(3)
                self.vert.insert(0, new)
            self.horiz[0], self.horiz[2] = self.vert[0],self.vert[2]  # top and bottom on horizontal track set to new bottom
            self.y = (self.y + dy) % 11
        elif face[1] != 0:  # movement is regarding x, horizontal face changed
            dx = face[1]
            if dx == -1: #left
                cur = self.horiz.pop(0)
                self.horiz.append(cur)
            elif dx == 1: #right
                new = self.horiz.pop(3)
                self.horiz.insert(0, new)
            self.vert[0], self.vert[2] = self.horiz[0],self.horiz[2]  # top and bottom on vertical track set to new top, bottom
            self.x = (self.x + dx) % 11


grid = [[1] * 11] * 4
for i in range(0, 3):
    row = [int(x) for x in input().split()]
    nRow = [1, 1, 1, 1] + row + [1, 1, 1, 1]
    # print(nRow)
    grid.append(nRow)

grid += [[1] * 11] * 4
#for row in grid:
    #print(" ".join([str(x) for x in row]))


def drawGrid(aDice, grid):
    cY, cX = aDice.coords()
    for dy in range(-1, 2,):
        row = ""
        for dx in range(-1, 2):
            if 0 <= cY + dy < 11 and 0 <= cX + dx < 11:
                row += str(grid[cY + dy][cX + dx])
            else:
                row += "X"
        print(row)

def printGrid(grid,dice):
    for row in grid:
        print(" ".join([str(f) for f in row]))
    print(dice.x,dice.y)
dice = dice()
n = int(input())
while n != 0:
    for i in range(n):
        print("top", dice.top())
        y, x = dice.coords()
        print("coords",y,x )
        print("Current", grid[y][x])
        cNum = (dice.top() + grid[y][x])
        heading = dice.heading
        print("Currently facing ",directions[heading])
        if cNum > 6:
            cNum -= 6
        print("Changing {} to {}".format(grid[y][x], cNum))
        grid[y][x] = cNum
        if cNum == 1 or cNum == 6:
            dice.move(faces[dice.heading])
        elif cNum == 2:
            moveToDo = (heading + 1) % 4
            dice.setHeading(moveToDo)
            dice.move(faces[moveToDo])
        elif cNum == 3 or cNum == 4:
            moveToDo = (heading + 2) % 4
            dice.setHeading(moveToDo)
            dice.move(faces[moveToDo])
        elif cNum == 5:
            moveToDo = (heading - 1) % 4
            dice.setHeading(moveToDo)
            dice.move(faces[moveToDo])
        print("horiz",dice.horiz)
        print("vert",dice.vert)
        printGrid(grid,dice)
        #print(dice.coords())
    #print(dice.coords())
    drawGrid(dice, grid)
    n = int(input())

