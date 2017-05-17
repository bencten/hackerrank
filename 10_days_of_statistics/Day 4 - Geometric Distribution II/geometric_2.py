# geometric_distribution_formula = q^(n-1) * p
# where   n = number of trials
#         q = failure ratio
#         p = success ratio

# in_prob = [1, 3]
#
# p = 1 / 3
# q = 1 - p
# n = 5
# g = 0
#
#
# def geo(n):
#     prob = q ** (n - 1) * p
#     return prob
#
#
# for x in range(5+1):
#     g = geo(x+1) + g


n = 5

p = 1/3
q = 2/3

probability = 0
for x in range(1, 6):
    probability = probability + q**(x-1) * p

print("%.3f" % probability)

print("{0:.3f}".format(g))
