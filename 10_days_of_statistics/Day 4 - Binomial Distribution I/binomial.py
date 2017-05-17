# binomial_distribution_formula = n!/(x! * (n-x)!) * p^x * q^(n-x)
# where   n = number of trials
#         x = number of successes
#         q = failure ratio
#         p = success ratio


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

# user_input = raw_input()
# user_input = "1.09 1"
# user_input = user_input.split(' ')
prob = 1.09 / 100.0
trials = 1
print(prob)

def pdf(x, n, r):
    bi_coeff = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    return bi_coeff * (math.pow(prob, x)) * (math.pow(1 - prob, n - x))


ans_1 = pdf(0, trials, prob) + pdf(1, trials, prob) + pdf(2, trials, prob)
ans_2 = sum([pdf(j, trials, prob) for j in range(2, 11)])

print(round(ans_1, 3))
print(round(ans_2, 3))
