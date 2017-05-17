import math

# mean = input()
# k = input()
mean = 2.5
k = 5


def poisson(k, mean):
    out = math.pow(mean, k) * math.pow(math.e, -1 * mean) / math.factorial(k)
    return float(out)


print("{0:3f}".format(poisson(k, mean)))


