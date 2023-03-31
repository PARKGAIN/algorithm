N = int(input())
K = int(input())
arr = [i for i in range(1,N+1)]
ans = []
pt = 0
for _ in range(N):
  pt += K - 1 
  pt %= len(arr)
  ans.append(arr.pop(pt))
  
print(f"<{','.join(map(str,ans))}>")
