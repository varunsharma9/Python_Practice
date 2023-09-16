try:
  f = open("D:\\data.txt")
except FileNotFoundError:
  print("the given file is not present in the system  ")
finally:
  print("closing the file")
  try:
    f.close()
  except NameError:
    print("not available in system ")
  

