# x = open("write.txt",'r')
# x.write("the given element is not from differ category ")
# a = x.read()
# print(a)
# x.close

try:
  y = open("write.txt",'r')
except FileNotFoundError:
  print("the file is not present in the system")
finally:
  print("yes the file is present in it , now we are moving to close it")
  try:
    y.close
  except NameError:
    print("this file dosent have anything in it ")