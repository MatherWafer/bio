from collections import defaultdict
from copy import deepcopy

def dot():
    return "."

class piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def coords(self):
        return self.y, self.x


class team:
    def __init__(self, count, order, startCoord, colour):
        self.colour = colour
        self.count = count
        self.order = order
        self.pieces = [piece(i, startCoord) for i in range(0, 5)]

    @property
    def currentPiece(self):
        return self.pieces[self.order[self.count] - 1]


class grid:
    def __init__(self, teams):
        self.grid = [defaultdict(dot) for i in range(0, 5)]
        self.neut = piece(2, 2)
        self.teams = teams

    def getGrid(self):
        for i in range(0, 5):
            for j in range(0, 5):
                for team in self.teams:
                    if (j, i) in [p.coords for p in team.pieces]:
                        #print("Found", team.colour, "at", (j, i))
                        self.grid[j][i] = team.colour
                    elif (j, i) == self.neut.coords:
                        self.grid[j][i] = '*'
        return self.grid

    def checkMove(self, nPiece, direction):
        dy, dx = direction
        if 0 <= nPiece.x + dx < 5 and 0 <= nPiece.y + dy < 5:
            if self.grid[nPiece.y + dy][nPiece.x + dx] == ".":
                return True
        return False

    def move(self, piece2, direction):
        dy, dx = direction
        f = self.getGrid()
        while 0 <= piece2.x + dx < 5 and 0 <= piece2.y + dy < 5 and f[piece2.y + dy][piece2.x + dx] == ".":
            self.grid[piece2.y][piece2.x] = "."
            piece2.y += dy
            piece2.x += dx
        self.grid = self.getGrid()
        return piece2.y

    def fullMove(self,piece1,team):
        loseFace = None
        bestFace = []
        if team == 'F':
            lose = 4
            win = 0
        elif team == 'S':
            lose = 0
            win = 4
        for face in directions:
            oppositeFace = [face[0] * -1,face[1]*-1]
            nBoard = deepcopy(self)
            if self.checkMove(self.neut,face):
                if win == nBoard.move(nBoard.neut,face):
                    self.move(self.neut,face)
                    self.displayGrid()
                    print("Winning move")
                    exit()
                elif lose == nBoard.move(nBoard.neut,face):
                    loseFace = face
                else:
                    nBoard.move(nBoard.neut,face)
                    if True not in [nBoard.checkMove(piece1,face1) for face1 in directions]:
                        pass
                    elif True in [nBoard.checkMove(piece1,face1) for face1 in directions]:
                        bestFace.append(face)
        if bestFace:
            self.move(self.neut,bestFace[0])
            self.displayGrid()
            print("*"*30)
        else:
            if loseFace is not None:
                print("Losing move")
                self.move(self.neut,loseFace)
                self.displayGrid()
                exit()
        for face in directions:
            if self.checkMove(piece1,face):
                self.move(piece1,face)
                self.displayGrid()
                print("*"*30)
                break

    def displayGrid(self):
        for row in self.grid:
            print("".join([row[j] for j in range(0, 5)]))


directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
order1 = list(map(int, [s for s in input("Order 1").split(" ")]))
order2 = list(map(int, [e for e in input("Order 2").split(" ")]))
F = team(0, order1, 4, 'F')
S = team(0, order2, 0, 'S')

neut = piece(2, 2)

theBoard = grid([F, S])
f = theBoard.getGrid()

print(F.currentPiece.coords)

for h in [F,S]:
    print(h.colour)
    theBoard.fullMove(h.currentPiece,h.colour)
    h.count = (h.count + 1) % 5
    theBoard.displayGrid()

while True:
    for h in [F, S]:
        print("//{} next".format(h.colour))
        theBoard.fullMove(h.currentPiece, h.colour)
        h.count = (h.count + 1) % 5
"""
neut = [2, 2]


def setGrid(pieces1, pieces2, neut):
    grid = [defaultdict(dot) for i in range(0, 5)]
    for i in range(0, 5):
        for j in range(0, 5):
            if [i, j] in pieces1:
                grid[i][j] = 'F'
            elif [i, j] in pieces2:
                grid[i][j] = 'S'
            elif [i, j] == neut:
                grid[i][j] = '*'
    return grid


grid = setGrid(pieces[0], pieces[1], neut)


def displayGrid(grid):
    for row in grid:
        print("".join([row[j] for j in range(0,5)]))


displayGrid(grid)


def checkMove(coord, direction,grid):
    dx, dy = direction
    y, x = coord[0],coord[1]
    if 0 <= x + dx < 5 and 0 <= y + dy < 5:
        if grid[y + dy][x + dx] is None:
            return True
    else:
        return False


def move(coord, direction,grid):
    y, x = coord[0],coord[1]
    dy, dx = direction
    while 0 <= x + dx < 5 and 0 <= y + dy < 5 and grid[y + dy][x + dx] is None:
        x += dx
        y += dy
    return [y, x]


def checkWin(player):
    for face in directions:
        if move(neut, face,setGrid(pieces[0], pieces[1], neut))[0] == 4 * (player - 1):
            return [True, face]
    return [False,face]


def turn(player,neut):
    choice = player - 1
    moves = []
    canMove = False
    if checkWin(player)[0]:
        neut[0],neut[1] = move(neut,checkWin(player)[1],setGrid(pieces[0], pieces[1], neut))
        grid2 = setGrid(pieces[0], pieces[1], neut)
        displayGrid(setGrid(pieces[0], pieces[1], neut))
    else:
        for face in directions:
            if checkMove(neut,face,setGrid(pieces[0], pieces[1], neut)) and not checkWin(3 - player)[0]:
                neut[0],neut[1] = move(neut,face,setGrid(pieces[0], pieces[1], neut))
                grid = setGrid(pieces[0], pieces[1], neut)
                canMove = True
                break
        print("a")
        if not canMove:
            for face2 in directions:
                if checkMove(neut,face2,setGrid(pieces[0], pieces[1], neut)) and checkWin(3-player)[0]:
                    neut = move(neut,face2,setGrid(pieces[0], pieces[1], neut))
                    displayGrid(setGrid(pieces[0], pieces[1], neut))
                    exit()
        for face3 in directions:
            print(face3)
            if checkMove(pieces[choice][counts],face3,setGrid(pieces[0], pieces[1], neut)):
                pieces[choice][counts] = [int(x) for x in move(pieces[choice],face3,setGrid(pieces[0], pieces[1], neut))]
                print(pieces[choice],neut)
                displayGrid(setGrid(pieces[0], pieces[1], neut))


turn(1,neut)
displayGrid(setGrid(pieces[0], pieces[1], neut))
print(pieces[0])
print(pieces[1])
turn(2,neut)
displayGrid(setGrid(pieces[0], pieces[1], neut))
"""
# try if not for all values of face.
# then else condition moves neutron and then moves piece from direction as is needed, updating counters[0] and counters[1], need to draw grid.
