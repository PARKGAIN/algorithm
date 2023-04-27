A,B= map(str,input().split())
a=list(A)
b=list(B)
for left in range(len(a)//2):
  right=len(a)-left-1
  temp =a[left]
  a[left]= a[right]
  a[right]= temp

for left in range(len(b)//2):
  right=len(b)-left-1
  temp =b[left]
  b[left]= b[right]
  b[right]= temp
c=''.join(a)
d=''.join(b)
if (c>d):
  print(c)
else:
  print(d)
