C = int(input())
for i in range(C):
  S = list(map(int, input().split()))
  del S[0];
  average=sum(S)/len(S);
  a=[stu for stu in S if stu> average]
  T= len(a)/len(S)*100;
  print(f'{T:.3f}%');
