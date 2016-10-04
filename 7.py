A = []
c = 0
k = 0
for i in range(10):
    A.append(int(input()))
for i in range(9):
    if A[i] == 2 and A[i + 1] != 2:
        c += 1
for i in range(10):
    k += A[i]
p = (k - 2 * c) / (10 - c)
print(round(p, 0))
