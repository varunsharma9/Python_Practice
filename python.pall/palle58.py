try:
  x = int(input("enter the first numbere here : "))
  y = int(input("enter the second numbere here : "))
  z = x+y
except ValueError:
  print("please enterr the valid integer ")
try:
  print(z)
except:
  print("name error")