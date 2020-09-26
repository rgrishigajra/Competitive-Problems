
def find_letter_case_string_permutations(str):
    permutations = [str]
    for letter in range(len(str)):
        perm_len = len(permutations)
        if str[letter].isnumeric():
            continue
        for perm in range(perm_len):
            changed_str = permutations[perm][:letter] + \
                permutations[perm][letter].swapcase() + permutations[perm][letter+1:]
            permutations.append(changed_str)
    return permutations


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
