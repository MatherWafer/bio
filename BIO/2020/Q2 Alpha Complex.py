class room:
    def __init__(self):
        self.ent = False
        self.cons = {}
    def addCon(self,room):
        self.cons[room] = False

    def enter(self):
        invert(self.ent)

    def checkEmpty(self):
        if not self.cons:
            return True
        else:
            return False

    def printKeys(self):
        print("".join(sorted(self.cons.keys())))

    def move(self):
        rooms = sorted(self.cons.keys())
        if self.ent:
            invert(self.cons[rooms[0]])
            return rooms[0]
        else:
            for room in rooms:
                if self.cons[room]:
                    if room == rooms[-1]:
                        invert(rooms[-1])
                        return room
                    else:
                        next = rooms.index(room) + 1
                        invert(rooms[next])
                        return rooms[next]


plan = input().split()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(plan)+2]
out = [x for x in alpha if x not in plan]
rooms = {}
print(plan,out)

for letter in alpha:
    rooms[letter] = room()
seen = []
while plan:
    chosenRoom = plan[0]
    for nRoom in out:
        if nRoom not in seen:
            seen.append(nRoom)
            print("Connecting {} and {}".format(nRoom,chosenRoom))
            rooms[nRoom].addCon(chosenRoom)
            rooms[chosenRoom].addCon(nRoom)
            break
    plan.pop(0)
    out = sorted(out + [chosenRoom])
    print(out)

a,b = [x for x in alpha if x not in seen]
rooms[a].addCon(b)
rooms[b].addCon(a)

for room in rooms.keys():
    print(rooms[room].printKeys())

