vertStrip = [1, 2, 6, 5]
horizStrip = [1, 4, 6, 3]
from copy import deepcopy

faces = [(-1, 0), (0, 1), (1, 0), (0, -1)]
directions = ["up", "right", "down", "left"]
heading = 0


class dice:
    def __init__(self):
        self.y, self.x = 5, 5
        #self.vert = [1, 5, 6, 2]  # top,towards,bottom,away
        #self.horiz = [1, 4, 6, 3]  # top,right,bottom,left
        self.top = 1
        self.bottom = 6
        self.toward = 5
        self.away = 2
        self.left = 3
        self.right = 4
        self.heading = 0

    def getTop(self):
        return self.top

    def setHeading(self, newHeading):
        self.heading = newHeading

    def coords(self):
        return self.y, self.x

    def move(self, face):
        print("Moving", directions[faces.index(face)])
        if face[0] != 0:  # movement is regarding y, vertical face changed
            dy = face[0]
            if dy == -1:  # up -- Face going to bottom of board becomes top
                nD = deepcopy(self)
                temp1 = nD.top
                temp2 = nD.bottom# Top and bottom stored
                temp3 = nD.toward
                temp4 = nD.away
                self.top = temp3
                self.bottom = temp4
                self.toward = temp2
                self.away = temp1
            elif dy == 1:  # down -- Face going to top of board becomes top
                nD = deepcopy(self)
                temp1 = nD.top
                temp2 = nD.bottom
                temp3 = nD.toward
                temp4 = nD.away
                self.top = temp4
                self.bottom = temp3
                self.toward = temp1
                self.away = temp2
            self.y = (self.y + dy) % 11
        elif face[1] != 0:  # movement is regarding x, horizontal face changed
            dx = face[1]
            if dx == -1:  # left -- Right face becomes top.
                nD = deepcopy(self)
                temp1 = nD.top
                temp2 = nD.bottom
                temp3 = nD.left
                temp4 = nD.right
                self.top = temp4
                self.bottom = temp3
                self.left = temp1
                self.right = temp2
            elif dx == 1:  # right -- Left Face becomes Top
                nD = deepcopy(self)
                temp1 = nD.top
                temp2 = nD.bottom
                temp3 = nD.left
                temp4 = nD.right
                self.top = temp3
                self.bottom = temp4
                self.left = temp2
                self.right = temp1
            self.x = (self.x + dx) % 11


grid = [[1] * 11] * 4
for i in range(0, 3):
    row = [int(x) for x in input().split()]
    nRow = [1, 1, 1, 1] + row + [1, 1, 1, 1]
    # print(nRow)
    grid.append(nRow)

grid += [[1] * 11] * 4


# for row in grid:
# print(" ".join([str(x) for x in row]))


def drawGrid(aDice, grid):
    cY, cX = aDice.coords()
    for dy in range(-1, 2, ):
        row = ""
        for dx in range(-1, 2):
            if 0 <= cY + dy < 11 and 0 <= cX + dx < 11:
                row += str(grid[cY + dy][cX + dx])
            else:
                row += "X"
        print(row)


def printGrid(grid, dice):
    for i,row in enumerate(grid):
        if i == dice.y:
            print(" ".join([str(f) for f in row])+ "Dice at " , str(dice.x))
        else:
            print(" ".join([str(f) for f in row]))
    print(dice.x, dice.y)


dice = dice()
n = int(input())
while n != 0:
    for i in range(n):
        print("top", dice.getTop())
        print("Bottom",dice.bottom)
        print("Right",dice.right)
        print("Left",dice.left)
        print("Towards",dice.toward)
        print("Away",dice.away)
        y, x = dice.coords()
        print("coords", y, x)
        print("Current", grid[y][x])
        cNum = (dice.getTop() + grid[y][x])
        heading = dice.heading
        print("Currently facing ", directions[heading])
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

        printGrid(grid, dice)
        # print(dice.coords())
    # print(dice.coords())
    drawGrid(dice, grid)
    n = int(input())

