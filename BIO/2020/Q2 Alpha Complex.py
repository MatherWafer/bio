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
        print("ent =",self.ent)
        if self.ent:
            self.cons[roomsT[0]] = not self.cons[roomsT[0]]
            return roomsT[0]
        else:
            for roomf in roomsT:
                print(roomsT[-1])
                print(roomf)
                print(roomf,self.cons[roomf])
                if self.cons[roomf]:
                    if roomf == roomsT[-1]:
                        print("Last")
                        self.cons[roomsT[-1]] = not self.cons[roomsT[-1]]
                        return roomf
                    else:
                        print("Not last, goigng to next")
                        next = roomsT.index(roomf) + 1
                        print(roomsT[next])
                        self.cons[roomsT[next]] = not self.cons[roomsT[next]]
                        return roomsT[next]
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

out = [x for x in alpha if x not in plan]
rooms = {}

for letter in alpha:
    rooms[letter] = room()
seen = []
while plan:
    chosenRoom = plan[0]
    for nRoom in out:
        if nRoom not in seen:
            seen.append(nRoom)
            rooms[nRoom].addCon(chosenRoom)
            rooms[chosenRoom].addCon(nRoom)
            break
    plan.pop(0)
    out = sorted(out + [chosenRoom])

a, b = [x for x in alpha if x not in seen]
rooms[a].addCon(b)
rooms[b].addCon(a)

agent1 = agent()

agent1.moveIn("A")
rooms["A"].enter()
print(rooms["A"].ent)
endPos = ""
for room in rooms:
    rooms[room].printKeys()

for i in range(0,max(int(p),int(q))):
    newRoom = rooms[agent1.getPos()].move()
    print(newRoom,"newroom")
    agent1.moveIn(newRoom)
    rooms[newRoom].enter()
    if i+1 == int(p) or i + 1 == int(q):
        endPos += agent1.getPos()

print(endPos)