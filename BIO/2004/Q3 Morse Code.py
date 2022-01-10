letters = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"...."
,"i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-",
"r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
morseToLetter ={}
for key in letters:
    morseToLetter[letters[key]] = key

def conv(word):
    morse = ""
    for char in word:
        morse += letters[char]
    return morse

word = input()
morse = conv(word)
cLeft  = len(morse)

def solve(phrase,left):
    print("phrase",phrase,left,"left")
    if len(phrase) > left * 4:
        return 0
    if len(phrase) == 0 and left == 0:
        return 1
    score = 0
    for i in range(4):
        if i <= len(phrase):
            chunk = phrase[:i]
            print(chunk)
            if chunk in morseToLetter.keys():
                if i+1 == len(phrase):
                    score += solve("",left-1)
                else:
                    score += solve(phrase[i:],left-1)
    return score


print(solve(morse,cLeft))
