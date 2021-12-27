def getWheel(n):
    wheel1 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    wheel2 = []
    count = n - 1
    count %= len(wheel1)
    for i in range(0, 26):
        letter = wheel1.pop(count)
        count += n - 1
        try:
            count %= len(wheel1)
        except:
            print("Wheel finished")
        wheel2.append(letter)
    return wheel2

def encrypt(wheel, word):
    print(''.join(wheel[:6]))
    wList = list(word)
    eList = []
    for letter in wList:
        eList.append(wheel[ord(letter) - ord('A')])
        temp = wheel.pop(0)
        wheel.append(temp)
    return str(''.join(eList))

"""
skip = int(input("skip"))
word = input("bjizzums")
"""
print(encrypt(getWheel(999999), 'MOON'))





