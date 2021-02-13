import math
import os
import random
import re
import sys


#
# Complete the 'getPotentialDomains' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY lines as parameter.
#

def getPotentialDomains(lines):
    # Write your code here
    # print(lines)
    regex_pattern = r'http(s?)://(?:www.|ww2.|web.)?(([a-zA-Z0-9_-]+\.)+[a-zA-Z]+)'
    l = []
    for line in lines:
        if re.search(regex_pattern, line):
            for match in re.findall(regex_pattern, line):
                l.append(match[1])

    ans = ';'.join(sorted(set(l)))

    return ans


if _name_ == '_main_':
