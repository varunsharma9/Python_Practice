a =  int(input("enter the number "))
if a%3 == 0 and a%5 == 0 and a%10 == 0:
  print("the given number is divisable by 3,5 and 10")
elif a%3 == 0 and a%5 == 0:
  print("the given number is divisable by 3 and 5 ")
elif a%3 == 0:
  print("the given number is divisable by 3 only ")
elif a%5 == 0:
  print("the given number is divisable by 5 only ")
else:
  print("the given input is not fit in our conditions ")