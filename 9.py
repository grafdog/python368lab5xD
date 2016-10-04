n = int(input())
a = list(map(int, input().split()))
b = int(input())
l = 0
for i in range(n-b+1):
    for k in range(b-1):
      s = a[i+k] + a[i]
    if s > l:
        l = s
print(l)