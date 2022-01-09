
n = int(input())


def digitsN(n):
    if n == 1:
        return 1,1
    n -= 1
    digits = 2
    combs = 9 ** (digits //2)
    while combs < n:
        n -= combs
        digits +=1
        combs = 9 ** (digits // 2)
    return digits,n


digits, n = digitsN(n)
leftDigits = digits // 2


def buildLeft(digits,n):
    if digits == 0:
        return ""
    for i in range(1,10):
        if 9 **(digits-1) >= n:
            return str(i) + buildLeft(digits-1,n)
        n -= 9 **(digits - 1)


left = buildLeft(leftDigits,n)
if digits % 2 == 0:
    mid = ""
else:
    mid = "5"
right = "".join([str(10 - int(x)) for x in reversed(left)])
print(left+mid+right)
