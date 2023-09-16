# def sampel1 (fun,name):
#   fun(name)
# def sampel2(name):
#   print(name)

# sampel1(sampel2,"python")


def costume_decorator(fun):
  def inner_function():
    print("****************************")
    fun()
    print("****************************")
  return inner_function

@costume_decorator
def sampel1():
  print("HI VARUN")
sampel1()

@costume_decorator
def sampel2():
  print("HI RAGHAV")
sampel2()

@costume_decorator
def sampel3():
  print("HI RAMAN")
sampel3()