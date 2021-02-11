n = input()
nums = input()
list_nums = nums.split(' ')
# list_nums = ['3','1000','1333','47']

def sieve(n):
  isprime = [False, False] + [True]*n
  for p in range(2,n):
    if isprime[p]:
      for kp in range(2*p,n,p):
        isprime[kp] = False
  return isprime

isprime = sieve(100000)

ans = [ 'Prime' if isprime[int(e)] else 'Composite' for e in list_nums]
print(' '.join(ans))
