# def f1(x):
#   return x**2
# res = f1(int(input("enter the numbere which's square you do want,here : ")))
# print(res)
##################   alternative method lambda ####################

f1 = lambda x : x**2+x**3
res = f1(int(input('enter the number for the opereation here : ')))
print("addation of square of given num and addation of cube of the same given number is",res)