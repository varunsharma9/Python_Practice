l = [2,1,3,5,4]
even = 0
odd = 0
sum = 0
for i in l:
  if i%2 == 0:
    even = even + 1
    sum1 = sum + i
  else:
    odd = odd + 1
    sum2 = sum + i
print(even)
print(odd)
print(sum1)
print(sum2)

