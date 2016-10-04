N = int(input())
a = []
b = []
c =0
for i in range (N) :
  a.append(int(input()))
  b.append(int(input()))
T = int(input())
for i in range (N):
  if a[i] <= T and T <= b[i]:
    c +=1
print(c)