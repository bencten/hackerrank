import math

mean, std = input().split(' ')
mean, std = float(mean), float(std)
hours = float(input())
range_a, range_b = input().split(' ')
range_a, range_b = float(range_a), float(range_b)

def cdf(x):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(hours)))
# Between 20 and 22
print('{:.3f}'.format(cdf(range_b) - cdf(range_a)))
