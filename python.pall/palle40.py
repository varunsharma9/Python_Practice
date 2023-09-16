l = []
l.append(1)
print(l)

l2 = []
l2.extend([1,2,3,4,5,6,7,8,9,0])
print(l2)

l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a=int(input("enter the index position "))
b=int(input("enter the value "))
l3.insert(a,b)
print(l3)

l4 = [1, 2, 3, 4, 5, 6, 7, 2, 9, 0]
a1=int(input("enter the value wich u want to remove "))
l4.remove(a1)
print(l4)