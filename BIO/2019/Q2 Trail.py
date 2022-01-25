t,i,m = input().split()
t,m = int(t),int(m)

faces = [(1,0),(0,1),(-1,0),(0,-1)] #up right down left



class explorer:
    def __init__(self,path,size):
        self.x = 0
        self.y = 0
        self.oldX = 2
        self.oldY = 2
        self.trail = []
        self.maxTrail = size
        self.face = 0
        self.path = path
        self.curMove = 0


    def updateTrail(self,coord):
        if len(self.trail) < self.maxTrail:
            self.trail.insert(0,coord)
        else:
            last = self.trail[-1]
            self.trail.remove(last)
            self.trail.insert(0,coord)


    def move(self):
        tryCount = 0
        self.oldX,self.oldY = self.x,self.y
        if self.path[self.curMove] == 'R':
            self.face = (self.face + 1) % 4
        elif self.path[self.curMove] == 'L':
            self.face = (self.face - 1) % 4
        dy,dx = faces[self.face]
        #print(self.trail)
        while (self.x+dx,self.y+dy) in self.trail and tryCount < 4:
            self.face = (self.face + 1) % 4
            dy,dx = faces[self.face]
            tryCount += 1
        if tryCount == 4:
            print("({},{})".format(self.x,self.y))
            exit()
        self.x += dx
        self.y += dy
        self.updateTrail((self.oldX,self.oldY))
        self.curMove = (self.curMove + 1) % len(self.path)


explorer = explorer(i,t)
for i in range(m):
    explorer.move()

print("({},{})".format(explorer.x,explorer.y))

