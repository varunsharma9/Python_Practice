n = int(input("enter the number to cheack it is in list l or not "))
l = [85,665,35,24,6,57,6,9,4,6,47,46,47,8,29]
flag = True
for i in range(0,len(l),1):
  if l[i] == n:
    break
  else :
    flag = False
if flag == False:
  print(n," number is given in l list on index position " , i)
else :
  print(n," number is not given in l list ")
  

