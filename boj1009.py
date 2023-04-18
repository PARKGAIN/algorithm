T =int(input())
for i in range(0,T) :
  a, b = map(int, input().split()) 
  ans =1;
  for j in range(1,b+1):
    ans*=(a%10);
    ans%=10;
    if(ans == 0):
      ans=10;
  print(ans);
