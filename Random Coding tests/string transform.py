#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinTransform' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING source
#  2. STRING target
#
def getMinTransform(source, target):
    count = 0
    mapping= {}
    if source == target:
        return 0
    for index in range(len(source)):
        if source[index] not in mapping:
            mapping[source[index]] = target[index]
        elif mapping[source[index]] !=target[index]:
            return -1
    cycles = 0
    cycle_hash = {}
    for key in mapping:
        test = key
        if mapping[key] != key:
            while True:
                if mapping[test] in mapping and test not in cycle_hash:
                    test = mapping[test]
                    if key == test:
                        print(key)
                        cycles+=1
                        cycle_hash[key] = 1
                        break
                else:
                    break
    for key in mapping:
        if mapping[key] == key:
            continue
        if mapping[key] in mapping and mapping[mapping[key]] == key:
            count +=3
            cycles -=1
            mapping[mapping[key]] = mapping[key]
        else:
            count+=1
    return count+cycles

if _name_ == '_main_':

s = 'abc'
t = 'cab'

# s='abcde'
# t = 'bcdef'
# t = 'tiktok'
# s = 'siksok'

# s = 'aaa'
# t = 'bbb'

# s = 'ababcc'
# t = 'cccccc'

s = 'ab'
t = 'ba'

# s = 'abac'
# t = 'wxyz'
print(canConvert(s, t))
