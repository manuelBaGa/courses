#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
# SAMPLE
#
#
# STDIN           Function
# -----           --------
# 5               X[] and W[] size n = 5
# 10 40 30 50 20  X = [10, 40, 30, 50, 20]  
# 1 2 3 4 5       W = [1, 2, 3, 4, 5]

def weightedMean(X, W):
    # Write your code here
    weight_scores_sum = [ X[i] * W[i] for i in range(len(X)) ]
    return print(round(sum(weight_scores_sum)/sum(W),1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
