N = int(input())
K = int(input())
arr = list(range(N + 1))
ans = []
pt = 0
for _ in range(N):
  pt += K - 1  #인덱스!
  pt %= len(arr)
  ans.append(arr.pop(pt))

print(*ans)
