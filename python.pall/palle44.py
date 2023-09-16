# #list comprihension 

l = [i for i in range (1,11)]
print(l)

m = [i for i in range (2,30,2)]
print(m)

n = [i for i in range(0,101,10)]
print(n)

print(".......................................................................................")

m1=[1,2,3,4,56,78,8,9,6,]
m2=[]
for i in m1:
  m2.append(i)
print(m2)  

l1=[434,352,235,476,235,459,5225,344,322,545,443,345,532]
l2=[i for i in l1]
print(l2)  

a1 = [22,42,23411,43,233,23,42,4,34,23,47,42,33,44,2,34,2,23,232]
a2 = [i for i in a1 if i%2==0]
print(a2)