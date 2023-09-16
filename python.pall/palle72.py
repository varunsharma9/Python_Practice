# nested function (function inside function)
def f1():
  def f2():
    print("inner function ")
  print("outer function")

f1()

# returning and function inside another function 
def f1():
  def f2():
    print("inner function ")
  print("outer function")
  return f2
fun = f1()
print(fun)  #it will give the address of the inner function 
fun()

