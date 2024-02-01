n = int(input('desimal: '))
 
a = []
i = 0
while n > 0:
  a.append(n % 2)
  n = n // 2
  i = i+1

print('biner: ',end=' ')

 
for i in range(i-1,-1,-1):
  print(a[i],end='')


