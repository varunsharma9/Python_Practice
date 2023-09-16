#filter method 
x = [10,23,34,45,52,55,73,62,53,57]
a = list(filter(lambda i : i%2 == 0 ,x))
print(a)

x1 = [213,3442,34,624,563,575,7456,85,735,6,72,46,25,73573,57,357,]
b = list(filter(lambda i : i % 2 != 0,x1))
print(b)

x2 = [51,52,53,54,55,56,57,58,59,60]
c = list(filter(lambda i : i % 2 != 0,x2))
print(c)

x3 = [213,3442,34,624,563,575,7456,85,735,6,72,46,25,73573,57,357,]
d = list(filter(lambda i : i>=500 and i<=1000,x3))
print(d)

