def get_primes(n):
  a= [False,False]+ [True]*(n-1)
  primes=[]
  for i in range(2,n+1):
    if a[i]:
      primes.append(i)
      for j in range(2*i,n+1,i):
        a[j]=False
  return primes

T = int(input())
primes = get_primes(10000) 

for _ in range(T):
  n = int(input())
  for p1 in reversed(primes):
    if p1 > n//2:
      continue
    p2 = n - p1
    if p2 in primes:
      print(p1,p2)
      break
