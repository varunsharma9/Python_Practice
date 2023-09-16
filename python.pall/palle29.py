#print the lenngth of l , addation of 
l = [35,23,53,4,3,44,6,6,44,6,7,5,4,5,8,6,53,4,35]
e = 0
o = 0
sum = 0
for i in l:
  if i%2 == 0:
    print(i)
    e =  e + 1
    sum = sum + i
print("..............")
print("total length of l is >-> ",len(l))
print("total even no present in l >-> ",e)
print("total addation of all the 'l' list >-> ",sum)