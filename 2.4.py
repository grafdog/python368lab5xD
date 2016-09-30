a = list(map(int, input().split()))
k = 1
for i in range(len(a)):
    if a.count(i) > k:
        k = a.count(i)
        m = i

print(m)