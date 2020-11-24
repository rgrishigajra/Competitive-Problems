#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'rpg' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#

def rpg(n, m, k):
    if k==0 or m==0:
        return 0
    p = 0
    recursive_records= {}
    def helper(n,m,k):
        count = 0
        if k==0:
            if n<=0:
                return 1
            else:
                return 0
        for i in range(m+1):
            if (n-i,k-1) in recursive_records:
                count+=recursive_records[(n-i,k-1)]
            else:
                output=helper(n-i,m,k-1)
                recursive_records[(n-i,k-1)] = output
                count+=output
        return count
    count = helper(n,m,k)
    p = round(count/((m+1)**k),5)
    if p != 0:
        return p
    return '{:0.5f}'.format(0)
    

if _name_ == '_main_':