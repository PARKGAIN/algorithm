N = int(input())
sum = 0
for i in range(1, N+1):
    a = []
    while i != 0:
        a.append(i % 10)
        i = i // 10
    if len(a) < 3:
        sum += 1
    else:
        is_hansu = True
        diff = a[1] - a[0]
        for x in range(2, len(a)):
            if a[x] - a[x-1] != diff:
                is_hansu = False
                break
        if is_hansu:
            sum += 1
print(sum)
