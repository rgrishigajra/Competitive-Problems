
def convert(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
             'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in roman:
            num += roman[s[i:i+2]]
            i += 2
        else:
            # print(i)
            num += roman[s[i]]
            i += 1
    return num


def solve(names):
    mapped = []
    for raw in names:
        name, num = raw.split()
        num = convert(num)  # this is from leetcode
        mapped.append((name, num, raw))
    mapped.sort(key=lambda x: [x[0], x[1]], reverse=False)
    print(names,mapped)
    return list(map(lambda x: x[2], mapped))


print(solve(names=['Louis IX', 'Louis VIII', 'Maria III', 'Oscar IV', 'Adams XXX', 'Anuar III', 'Maria III', 'Oscar V']
            ))
