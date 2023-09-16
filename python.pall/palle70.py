# MAP method in python 

x = [213,3442,34,624,563,575,7456,85,735,6,72,46,25,73573,57,357,453]
y = list(map(lambda i : i % 2 == 0,x))
print(y)

x1 = [81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
y1 = list(map(lambda i : i % 2 != 0,x))
print(y1)

x2 = [81,82,83,84,85,86,87,88,89,90]
y2 = list(map(lambda i : i**2 ,x2))
print(y2)

x3 = [81,82,83,84,85,86,87,88,89,90]
y3 = list(map(lambda i : i**3 ,x3))
print(y3)