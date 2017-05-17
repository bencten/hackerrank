"""
Objective 
In this challenge, we practice calculating the mean, median, and mode. 
"""



# n = input()
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

import numpy as np
from scipy import stats

def stats(arr):

    nums = np.array(arr)
    print(np.average(nums))
    print(np.median(nums))
    print(''.join(str(n) for n in (stats.mode(nums)[0])))



if __name__ == "__main__":
    arr = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
    stats(arr)