#lambda function - square of a number (1)

# def f1(x):
# return x**2
# res = f1(34)
# print(res)

a = lambda x : x**2
res = a(int(input("enter the number to ")))
print(res)