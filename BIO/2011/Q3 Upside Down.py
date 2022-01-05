
n = int(input())


def digitsN(n):
    if n == 1:
        return 1,1
    n -= 1
    digits = 2
    combs = 9 ** (digits //2)
    print(digits,combs)
    while combs < n:
        n -= combs
        digits +=1
        combs = 9 ** (digits // 2)
    return digits,n

digits, n = digitsN(n)

leftDigits = digits // 2
print("{}th number with {} digits".format(n,digits))


def buildLeft(digits,n):
    if digits == 0:
        return ""
    if digits == 1:
        for i in range(1,10):
            if i == n:
                return i
    for i in range(1,10):
        if 9 ** digits >= n:
            return str(i) + buildLeft(digits-1,n)
        n -= 9 ** digits

print(buildLeft(leftDigits,n))