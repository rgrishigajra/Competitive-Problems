def sieve(n):
  isprime = [False, False] + [True]*n
  for p in range(2,n):
    if isprime[p]:
      for kp in range(2*p,n,p):
        isprime[kp] = False
  return isprime

isprime = sieve(1000000)

# Dynamic programming
# C[i] = number of ways to split S[:i] into primes
def dp(s):
  C = [0]*(len(s)+1)
  for i in range(1,len(s)+1):
    C[i] = sum(C[j] for j in range(i) if isprime[int(s[j:i])]) 
    C[i] += isprime[int(s[:i])]
  return C[len(s)]

print(dp('3175'))