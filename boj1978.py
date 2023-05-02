N = int(input())
arr = list(map(int, input().split()))

def isSosu(x):
  if x < 2:
    return False
  for i in range(2, int(x**0.5)+1):
    if x % i == 0:
      return False
  return True

ans = list(filter(isSosu, arr))
print(len(ans))
