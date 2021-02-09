def primeCombination(num_str, lookup):
    if num_str not in lookup:
        total = 0

        for i in range(len(num_str)):
            if isPrime(num_str[:i+1]):
                if i+1 == len(num_str):
                    total += 1
                else:
                    total += primeCombination(num_str[i+1:], lookup)
        lookup[num_str] = total

    return lookup[num_str]


def isPrime(n_str):
    n = int(n_str)
    if n < 2:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


primeCombination('11375', {})
