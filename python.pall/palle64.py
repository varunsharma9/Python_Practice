#lambda method - addation of two numbers 

# def add (x,y):
#   sum = x + y 
#   print(sum)
# add(45,23)

a = lambda x,y : x + y
a1 = int(input("enter the first number here : "))
a2 = int(input("enter the second number here : "))
b = a(a1,a2) 
print(b)