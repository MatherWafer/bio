dic = {"a":	".-", "h": "....", "o": "---", "v": "...-",
    "b":"-...",	"i": "..",	"p": ".--.", "w": ".--",
    "c":"-.-.",	"j": ".---", "q": "--.-", "x": "-..-",
    "d":"-..", "k": "-.-", "r": ".-.", "y": "-.--",
    "e":".", "l": ".-..", "s": "...", "z": "--..",
    "f":"..-.", "m": "--", "t": "-",
    "g":"--.", "n": "-.", "u": "..-"}

alpha = "abcdefghijklmnopqrstuvwxyz"
word = input()
length = len(word)
import time
start = time.time()


def to_morse(data):
    ans = ""
    for i in data:
        ans += dic[i]
    return ans


def solve(cur, left):
    if left*4 < len(cur):
        return 0
    if left==0:
        if len(cur)==0:
            return 1
        else:
            return 0
    total = 0
    for possible in range(1,5):
        if possible <= len(cur):
            check = cur[:possible]
            if check in dic.values():
                total += solve(cur[possible:], left-1)
    return total


morseWord = to_morse(word)
#print(morseWord)


print(solve(morseWord, length))
print("EXECUTED IN", time.time()-start, "SECONDS")