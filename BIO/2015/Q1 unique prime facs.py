def factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


def primes(max):
    nums = [True] * max
    nums[0] = nums[1] = False
    for (num, prime) in enumerate(nums):
        if prime:
            yield num
            for x in range(num ** 2, max, num):
                nums[x] = False


num = int(input())
pFactors = [factor for factor in factors(num) if factor in primes(max(factors(num)))]

print(pFactors)
total = 1
for num in pFactors:
    total *= num
print(total)
