def getTime(initial,speed):
    hour = initial[0]
    minute = initial[1]
    newMins = (minute + speed) % 60
    addedHours = (minute + speed) // 60
    newHours = (hour + addedHours) % 24
    return newHours,newMins


t1 = [0,0]
t2 = [0,0]
speed1,speed2 = [int(s) for s in input("Speds 1 and 2").split(" ")]
t1 = getTime(t1,speed1)
t2 = getTime(t2,speed2)

while t1 != t2:
    t1 = getTime(t1,speed1)
    t2 = getTime(t2,speed2)
h,m = [list(str(s)) for s in t1]

if len(h) < 2:
    h.insert(0,"0")
if len(m) < 2:
    m.insert(0,"0")

print("".join([str(s) for s in h]) + ":" + "".join([str(t) for t in m]))