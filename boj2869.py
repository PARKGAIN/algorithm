A,B,V =map(int,input().split())
d,n= divmod((V-B),(A-B))
if(n>0):
  print(d+1)
else:
  print(d)
