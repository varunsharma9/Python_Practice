#try and except method 

try:
  x = [10,20,30,40,50]
  print(x[0])
  print(x[1])
  print(x[2])
  print(x[7])
except IndexError:
  print("value for the given index is not present in the list 'x' ")
  print(x[3])