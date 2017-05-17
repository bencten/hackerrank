import math



maxn = int(input().strip())
n = int(input().strip())
mean = int(input().strip())
sd = int(input().strip())


def cdf(u, d, x):
    return (math.erf((x - u) / (d * math.sqrt(2))) + 1) / 2


mean_dash = n * mean
sd_dash = math.sqrt(n) * sd

res = cdf(mean_dash, sd_dash, maxn)

