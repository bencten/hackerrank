from math import *

# geometric_distribution_formula = q^(n-1) * p
# where   n = number of trials
#         q = failure ratio
#         p = success ratio

in_prob = [1,3]

p = 1/3
q = 1 - p
n = 5



def geo():
    prob = q ** (n - 1) * p
    return prob

print("{0:.3f}".format(geo()))