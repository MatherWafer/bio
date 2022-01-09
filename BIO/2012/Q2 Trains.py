class station:
    def __init__(self,allCons):
        self.lazy = True
        self.cons = (allCons[1], allCons[2])
        self.straight = allCons[0]
        self.dir = 0  # 0 = Left, 1 = Right

    def setFlip(self):
        self.lazy = not self.lazy

    def move(self, entry):
        if entry == self.straight:
            if self.lazy:
                return self.cons[self.dir]
            else:
                temp = self.dir
                self.dir = (self.dir + 1) % 2
                return self.cons[temp]
        else:
            if self.lazy:
                self.dir = self.cons.index(entry)
            return self.straight


stations = {"A": station("DEF"),"B":station("CGH"),"C":station("BIJ"),"D":station("AKL")
    ,"E":station("AMN"),"F":station("ANO"),"G":station("BOP"),"H":station("BPQ"),"I":station("CQR"),"J":station("CRS"),"K":station("DST"),"L":station("DTM"),
    "M": station("ULE"),"N":station("UEF"),"O":station("VFG"),"P":station("VGH"),"Q":station("WHI"),"R":station("WIJ"),"S":station("XJK"),"T":station("XKL"),
            "U":station("VMN"),"V":station("UOP"),"W":station("XQR"),"X":station("WST"),}

flipFlops = input()
for x in flipFlops:
    stations[x].setFlip()

last,headed = [x for x in input()]
n = int(input())

for i in range(0,n):
    temp = headed
    headed = stations[headed].move(last)
    last = temp
print(last+headed)

