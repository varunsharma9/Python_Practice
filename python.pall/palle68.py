#lambda by two method to calling the function 

# def f1 (fun):
#   fun ()
# def f2():
#   print("hiiiiiiiiiiiiii")
# f1(f2)


def f1(fun):
  return fun()

f2 = lambda : "hiiiiiiii"   # first example 
a = f1(f2)
print(a)


# alternative 
 
def f(fun):
  return fun()

b = f1(lambda :"helloooooo")    # second example 
print(b)