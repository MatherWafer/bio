from collections import defaultdict


def patch():
    return "."


def makeField(pig,farmer,trees):
    field = []
    pX,pY = pig[0],pig[1]
    fX,fY = farmer[0],farmer[1]
    for i in range(0, 10):
        row = defaultdict(patch)
        for j in range(0, 10):
            if (j+1,i+1) == (pX,pY) == (fX,fY):
                row[j] = '+'
            elif (j+1, i+1) == (pX, pY):
                row[j] = 'P'
            elif (j+1,i+1) == (fX,fY):
                row[j] = 'F'
            for pair in trees:
                tX,tY = pair[0],pair[1]
                if j+1 == tX and tY == i + 1:
                    row[j] = '*'
        field.append(row)
    return field


def move(x,y,face,field):
    dx,dy = moves[face]
    if 0 < x + dx < 11 and 0 < y + dy < 11 and field[y+dy - 1 ][x + dx - 1] != "*":
        x += dx
        y += dy
    else:
        face = (face + 1) % 4
    return x,y,face


def displayField(field):
    for i in range(9,-1,-1):
        print("".join([field[i][j] for j in range(0,10)]))

field = []
trees = []
command = ""
moves = [(0,1), (1,0), (0,-1), (-1,0)]
pD,fD = 0,0
pX,pY = [int(x) for x in input("pX,pY").split(" ")]
fX,fY = [int(x) for x in input("fX,fY").split(" ")]

displayField(makeField((pX,pY),(fX,fY),[]))
moveNo = 0
while command != "X":
    command = input("Enter step")
    if command[0] == 'T':
        n = int(command.split(" ")[1])
        for i in range(0,n):
            tX,tY = [int(x) for x in input("tX,tY").split(" ")]
            trees.append((tX,tY))
        displayField(makeField((pX,pY),(fX,fY),trees))
    elif command[0] == 'M':
        moveNo += 1
        turns = int(command.split(" ")[1])
        for i in range(0,turns):
            field = makeField((pX,pY),(fX,fY),trees)
            pX,pY,pD = move(pX,pY,pD,field)
            fX,fY,fD = move(fX,fY,fD,field)
            if (pX,pY) == (fX,fY):
                print("Farmer and pigs meet on move",moveNo,"at",(pX,pY))
        field = makeField((pX,pY),(fX,fY),trees)
        displayField(field)


