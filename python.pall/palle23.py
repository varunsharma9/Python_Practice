foodType = input("enter the food type ")
timing = int(input("enter the timing  "))
if foodType == "breakfast":
  if timing in range(7,10):
    print("idli is in food")
  else:
    print("breakfast is finish ")
elif foodType == "lunch":
  if timing in range(12,14):
    print("you can have rice and daal today ")
  else:
    print("bro you are late for lunch ")
elif foodType == "dinner":
  if timing in range(15,17):
    print("today chapati and gobi is in dinner ")
  else:
    print("sorry! you are late for dinner ")
else:
  if foodType == "supper" and timing in range(18,19):
    print("cook can give you only coffee or tea ")
  else:
    print("nahaaaaa! the given input is wrong")