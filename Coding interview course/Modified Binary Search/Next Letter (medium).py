#  Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.
def search_next_letter(letters, key):
    l, h = 0, len(letters)-1
    if key > letters[h] or key < letters[0]:
        return letters[0]
    while l <= h:
        mid = (h+l)//2
        # mid points to element itself but we need next so we can elliminate this step!
        # if key == letters[mid]: 
        #     return letters[(mid+1) % (len(letters))]
        if key <= letters[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return letters[l % len(letters)]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
