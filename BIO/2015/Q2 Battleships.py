
class board:
    def __init__(self ,r ,a ,c ,m):
        self.r = r
        self.a = a
        self.c = c
        self.m = m
        self.grid = [[True for i in range(10)] for j in range(10)]

    def algo(self):
        self.r = (self.a * self.r + self.c) % self.m

    def printGrid(self):
        for row in self.grid:
            pRow = ""
            for square in row:
                if square:
                    pRow += "*"
                else:
                    pRow += "O"
            print(pRow)

    def checkAdj(self, x, y):
        #print("Checking for ",x,y)


        #self.printGrid()
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= y + dy < 10 and 0 <= x + dx < 10:
                    if not self.grid[y + dy][x + dx]:
                        #print("Collision at",(y+dy),(x+dx))
                        return False

        return True

    def place(self ,direc ,x ,y ,size):
        if direc == 'H':
            for i in range(size):
                #print( x +i)
                self.grid[y][x+i] = False
        elif direc == 'V':
            for i in range(size):
                self.grid[y+i][x] = False


    def check(self ,size):
        #print("r",self.r)
        self.algo()
        #print("R",self.r)
        if self.r < 10:
            y, x = 0,self.r
        else:
            last2 = int(str(self.r)[-2:])
            # print(last2)
            y, x = divmod(last2, 10)
        self.algo()
        #print(self.r)
        if self.r % 2 == 0:
            direc = "H"
        else:
            direc = "V"
        if direc == "H":
            for i in range(size):
                nX = x + i
                if nX >= 10:  # Out of Bounds
                    return False ,direc
                if not self.checkAdj(nX ,y):
                    # print("Collision around",nX,y)
                    return False ,direc
            return True ,direc ,x ,y
        elif direc == "V":
            for i in range(size):
                nY = y + i
                if nY >= 10:
                    return False ,direc
                if not self.checkAdj(x ,nY):
                    return False ,direc
            return True ,direc ,x ,y


ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
a ,c ,m = [int(x) for x in input().split()]
board = board(0 ,a ,c ,m)

for size in ships:
    nResult = board.check(size)
    result = nResult[0]
    while not result:
        nResult = board.check(size)
        # print(nResult)
        result = nResult[0]
    direc ,x ,y = nResult[1:]
    print(x ,y ,direc)
    board.place(direc ,x ,y ,size)
