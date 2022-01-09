coins = list(map(int,input("Coins").split()))
value = int(input("Value"))
ready = [False] * 11
from sys import maxsize


def find(value):
    values = [maxsize] * (value + 1)
    values[0] = 0
    for x in coins:
        for y in range(len(values)):
            if x <= y:
                values[y] = min(values[y],1 + values[y-x])
    return values[value] if values[value] != maxsize else -1

print(find(value))