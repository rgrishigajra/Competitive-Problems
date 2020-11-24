a = [2, 3, 4, 5, 7, 8, 5, 3, 2, 4, 6, 7, 7]
b = [13, 2, 2, 5, 7, 8, 9, 1, 89, 8]

from collections import defaultdict
def findCommon(a, b):
    res = []
    dic = defaultdict(int)
    if len(a) < len(b):
        hashing_list = a
        traversing_list = b
    else:
        hashing_list = b
        traversing_list = a
    for num in hashing_list:
        dic[num] += 1
    for num in traversing_list:
        if dic[num] > 0:
            res.append(num)
            dic[num] -=1
    res.sort()
    return res


print(findCommon(a, b))
