#enter the number by try and except method 

# try:
#   x = int(input("enter the first num ,here : "))
#   y = int(input("enter the second num ,here : "))
#   print(x+y)
# except ValueError:
#   print("please enter the valid integer")
# except NameError:
#   print("variable is not present")

try:
  x = int(input("enter the first num ,here : "))
  y = int(input("enter the second num ,here : "))
  z = x+y 
  print(z)
except ValueError:
  print("please enter the valid integer")
except NameError:
  print("variable is not present")