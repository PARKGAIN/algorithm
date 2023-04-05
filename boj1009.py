T = int(input())

for _ in range(T):
  a,b = map(int, input().split())
  temp=a%10
  if temp==0:
    print(10)
  elif temp in [1,5,6]:
    print(temp)
  elif temp in [4,9]:
    if b%2==0:
      print(temp*2%10)
    else:
      print(temp)
  else:
    b_temp = b%4
    if b_temp==0:
      print(temp**4%10)
    else:
      print(a**b%10)
