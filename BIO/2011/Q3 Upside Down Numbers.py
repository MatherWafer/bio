#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      l6mather
#
# Created:     05/01/2022
# Copyright:   (c) l6mather 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
n = int(input())
def digitsN(n):
    if n == 1:
        return 1,1
    n -= 1
    digits = 2
    combs = 9 ** (digits - 1)
    print(digits,combs)
    while combs < n:
        n -= combs
        digits +=1
        combs = 9 ** (digits - 1)
    return digits,n

digits, n = digitsN(n)

print("{}th number with {} digits".format(n,digits))