s = input()
charcount = [0]*26
perms = []
def getPerms(strin):
    if len(strin) == len(s):
        perms.append(strin)
        return
    for i in range(0,26):
        if charcount[i] > 0:
            charcount[i] -= 1
            getPerms(strin + chr(ord('a')+i))
            charcount[i] +=1


for c in s:
    charcount[ord(c)-ord('a')] +=1

print([x for x in charcount if x > 0])
getPerms("")
print(perms)