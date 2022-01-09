import time

def factorPair(num):
    pair = []
    for i in range(1,num//2 +1):
        if num % i == 0:
            if pair:
                if (i+num/i) < pair[0]+pair[1]:
                    pair = [int(i),int(num/i)]
            else:
                pair = [int(i),int(num/i)]
    return pair
n = int(input())
start = time.time()
mops = [float('inf')] * (n+2)
mops[0] = 0
mops[1] = 1
mops[2] = 2
for i in range(3,n+2):
    f,g = factorPair(i)
    mops[i] = min(mops[i-1] + 1,mops[f]+mops[g])

print(mops[n])
print(time.time()-start)