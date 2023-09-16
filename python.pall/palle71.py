#decorator 


# calling one method inside another method 
# def f1():
#   print("hiiii")
# def f2():
#   f1()
# f2()

# passing one function as a parameter to another function 
def f1(fun,name):
  result = fun(name)
  print(result)
def f2(name):
  return name

f1(f2,"varun")



