def getShortestFragment(strng):
    for k in range(1, len(strng)):
        for i in range(len(strng)-k+1):
            lowerSet = set()
            upperSet = set()
            temp = list(strng[i:i+k+1])
            for ch in temp:
                if ch.islower():
                    lowerSet.add(ch)
                else:
                    upperSet.add(ch)
                if(containsAllElements(lowerSet, upperSet) and containsAllElements(upperSet, lowerSet)):
                    value = str(k+1)
                    return value
    return "-1"


def containsAllElements(first, second):
    lower1 = set()
    lower2 = set()
    for e in first:
        lower1.add(e.lower())
    for e in second:
        lower2.add(e.lower())
    return all(elem in lower1 for elem in lower2)
