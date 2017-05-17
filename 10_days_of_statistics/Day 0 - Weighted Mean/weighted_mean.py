n = 5
arr_int = [10, 40, 30, 50, 2]
weights = [1, 2, 3, 4, 5,]


# for hackerank only
# n = int(input().strip())
#
# arr_int = [int(i) for i in input().strip().split(' ')]
# weights =  [int(i) for i in input().strip().split(' ')]



def weighted_mean(nums, weights):
    numerator = sum([nums * weights for nums, weights in zip(nums, weights)])
    denominator = sum(weights)
    return numerator / denominator


w_mean = weighted_mean(arr_int, weights)
print("{0:.1f}".format(w_mean))