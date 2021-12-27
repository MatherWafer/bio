import time
"""
def getPalin(digits):
    dig =[]
    if int(digits) % 2 == 0:
        for i in range (0,digits//2):
            dig.append(random.randint(0,9))
    num = 0
    for i in range(0,digits//2):
        num += dig[i]*10**i
    print(num)
    num = num * 10**(digits/2)
    num1=0
    for i in range(0,digits//2):
        print("i:" + str(i))
        print("dig[i]:" + str(dig[i]))
        #print(dig[i]*10**(digits//2-i))
        num1 += dig[i]*10**((digits//2-i)-1)
    print(int(num+num1))
    print(num1)
    print(dig.reverse())
    return
left = 0
right = 0
middle = None

left = random.randint(0,100000)
print(left)
left = list(int(x) for x in str(left))
right = []
for item in reversed(left):
    right.append(item)

print(*left)
print(*right)

print(left,right)
"""


def makePalin(num):
    numStr = str(num)
    mid = None
    if len(numStr) > 1:
        midIndex = len(numStr) // 2
        left = list(int(x) for x in numStr[:midIndex])
        if len(numStr) % 2 == 1:
            mid = numStr[midIndex]
    else:
        left = [num]
    #print(left)
    palinStr = ""
    leftStr = ""
    for numb in left:
        leftStr = leftStr + str(numb)
        #print("left:", leftStr)
    leftNum = int(leftStr)
    if mid is not None:
        palinStr = leftStr + mid
    for numb in reversed(left):
        palinStr = palinStr + str(numb)
        #print("New pal",palinStr)

    while int(palinStr) <= num:
        #print("Lower, finding next")
        if mid is not None:
            mid = int(mid)
            mid += 1
            if mid == 10:
                mid = 0
                leftNum += 1
            #print(leftNum)
            leftStr = str(leftNum)
            if mid is not None:
                palinStr = leftStr + str(mid) + leftStr[::-1]
            else:
                palinStr = leftStr + leftStr[::-1]
        else:
            if (leftNum + 1) % 10 == 0:
                mid = str(leftNum+1)[-1]
                leftStr = str(leftNum+1)[:-1]
            else:
                leftNum += 1
            #rint("LeftNum", leftNum)
            if len(numStr) > 1:
                leftStr = str(leftNum)
                if mid is not None:
                    palinStr = leftStr + mid + leftStr[::-1]
                else:
                    palinStr = leftStr + leftStr[::-1]
            else:
                palinStr = str(leftNum)
    #print(palinStr)

    print("Final Pal is" , int(palinStr))
    """
    print(mid)
    print(left)
    """
    return int(palinStr)

#num = int(input("Enter number"))


nums = [5,9,33,84,45653,3646000,24355343,123450000,234567890,678999876,99999999999999,999999999999999,123456789000000000,987654321123456789,9876543210123456789,9876543219123456789]
for num in nums:
    print(num)
    makePalin(num)
    time.sleep(0.2)

number = int(input("Enter num"))
palin = makePalin(number)
"""
if palin > number:
    print("W")
else:
    print("L")
"""
"""
num1 = 10**20 - 1
print(len(str(num1)))
print(num1)

print(num1-99999999988999999999)
num = 1
palins = []
sums = []
while num < 100000:
    palins.append(num)
    num = makePalin(num)

print(len(palins))

for i in range(0,917):
    for num in palins:
        sum = num + palins[i]
        if sum not in sums and sum <100000:
            sums.append(sum)
            print(sum)
print(len(sums))
"""


print(palins)
