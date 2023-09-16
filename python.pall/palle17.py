#Range Function in tuple , list and set
l = list(range(1,5))
print(l) #it will print list 
print(type(l))
print(len(l))
t = tuple(range(5,70,4))
print(t) #it will print tuple
print(type(t))
print(len(t))
s = set(range(-4,-45,5))
print(s) #it will print set
print(type(s))
print(len(s))
#now i am going to acces the value of the value of digits in list 
print("about list.................................................")
print("the value of the 1st index ",l[0])
print("the value of the 2nd index ",l[1])
print("the value of the 3rd index ",l[2])
print("the value of the 4th index ",l[3])
#now i am going to acces the value of the value of digits in tuple
print("about tuple.................................................")
print("the value of the 4th index ",t[3])
print("the value of the 4th index ",t[-3])
print("the value of the 4th index ",t[13])
print("the value of the 4th index ",t[4])
print("the value of the 4th index ",t[11])
print("the value of the 4th index ",t[9])
print("the value of the 4th index ",t[-4])
print("the value of the 4th index ",t[8])
print("the value of the 4th index ",t[-13])
print("the value of the 4th index ",t[16])
print("the value of the 4th index ",t[-7])
print("the value of the 4th index ",t[-11])
print("the value of the 4th index ",t[-2])
#now i am going to acces the value of the value of digits in set
print("about set.................................................")
#print("the value of the 4th index ",s[3])....................if we use it it will give errors because in set we cannot access the number by indexing 

 





