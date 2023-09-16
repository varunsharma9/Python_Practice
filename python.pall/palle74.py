# def costume_decorator(fun):
#   def inner_function():
#     print("----------------------------------------")
#     fun()
#     print("----------------------------------------")
#   return inner_function

# @costume_decorator
# def sampel1():
#   print("varun")
# sampel1()

# @costume_decorator
# def sampel2():
#   print("Raghav")
# sampel2()

# @costume_decorator
# def sampel3():
#   print("Tarun")
# sampel3()

# @costume_decorator
# def sampel4():
#   print("Arun")
# sampel4()

def costume_decorator(fun):
  def inner_function(name):
    print("----------------------------------------")
    fun(name)
    print("----------------------------------------")
  return inner_function

@costume_decorator
def sampel1(name):
  print(name)
sampel1("varun")