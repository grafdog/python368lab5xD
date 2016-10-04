i = 1
k = 0
l = 0
b = 0
n = 0
m = 0
while not i == 0:
    a = int(input())
    i = a
    if a == 0:
        break
    if a > k:
        l = l + 1
    else:
        if l > b:
            b = l
        l = 0
    if a < k:
        l = l + 1
    else:
        if l > b:
            b = l
        l = 0
    if a == k:
        l = 0
    k = a

print(max((l+1),(b+1)))

