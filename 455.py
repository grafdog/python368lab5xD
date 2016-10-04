a = 1 
b = 0 
c = 0 
i = 0 
while a!= 0: 
  a = int(input())
  if a>i:
     i,c = a,i
  if a>c and a<i:
     c = a
print(c)