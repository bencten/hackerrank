from math import sqrt

N = 5
numbers = [10, 40, 30, 50, 20]

# N = int(input())
# numbers = [int(x) for x in input().split()]

def std_dev():
    mean = sum(numbers) / N
    result = (sum([(number - mean) ** 2 for number in numbers]))/N
    out = sqrt(result)

    return out

print("{0:.1f}".format(std_dev()))



