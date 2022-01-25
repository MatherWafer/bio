def invert(bool):
    return not bool


class room:
    def __init__(self):
        self.ent = False
        self.cons = {}

    def addCon(self, room):
        self.cons[room] = False

    def enter(self):
        self.ent = not self.ent

    def printKeys(self):
        print("".join(sorted(self.cons.keys())))

    def move(self):
        roomsT = sorted(self.cons.keys())
        #print("ent =",self.ent)
        if self.ent:
            self.cons[roomsT[0]] = not self.cons[roomsT[0]]
            return roomsT[0]
        else:
            for i,roomf in enumerate(roomsT):
                #print(roomsT[-1])
                #print(roomf)
                #print(roomf,self.cons[roomf])
                if self.cons[roomf]:
                    if i == len(roomsT)-1:
                        #print("Last")
                        self.cons[roomsT[i]] = not self.cons[roomsT[i]]
                        return roomf
                    else:
                        #print("Not last, goigng to next")
                        #print(roomsT[i+1])
                        self.cons[roomsT[i+1]] = not self.cons[roomsT[i+1]]
                        return roomsT[i+1]
        print (self.cons.values())
        print("No cons")


class agent:
    def __init__(self):
        self.room = ""

    def getPos(self):
        return self.room

    def moveIn(self, newRoom):
        self.room = newRoom


plan,p,q = input().split()
plan = list(plan)

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(plan) + 2]
#print(alpha)
out = set(alpha) - set(plan)
#print(out)
rooms = {}

for letter in alpha:
    rooms[letter] = room()
seen = []
out = sorted(list(out))
while plan:
    chosenRoom = plan.pop(0)
    for nRoom in out:
        if nRoom not in seen and nRoom != chosenRoom:
            seen.append(nRoom)
            #print("Connecting {} and {}".format(nRoom,chosenRoom))
            rooms[nRoom].addCon(chosenRoom)
            rooms[chosenRoom].addCon(nRoom)
            break
    out = sorted(out + [chosenRoom])

a, b = list(set(alpha)-set(seen))
#print("Connecting",a,b)
rooms[a].addCon(b)
rooms[b].addCon(a)

agent1 = agent()

agent1.moveIn("A")
rooms["A"].enter()
#print(rooms["A"].ent)
endPos = ""
for room in rooms:
    rooms[room].printKeys()

for i in range(0,max(int(p),int(q))):
    newRoom = rooms[agent1.getPos()].move()
    #print(newRoom,"newroom")
    agent1.moveIn(newRoom)
    rooms[newRoom].enter()
    if i+1 == int(p) or i + 1 == int(q):
        endPos += agent1.getPos()

print(endPos)