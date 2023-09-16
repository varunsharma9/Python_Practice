#try and except method with ZeroDivisionError
try:
  x = int(input("enter the value of first numbere here : "))
  y = int(input("enter the value of second numbere here : "))
  z = x/y
  print(z)
except ZeroDivisionError:
  print("you cannot devide a number by zero ")
except ValueError:
  print("the value is not proper , thats why value error ")
try:
  print(z)
except NameError:
  print("please assign  variable properly ")
