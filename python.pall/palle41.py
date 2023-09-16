class Number :
  def __init__(self,value1,value2):
    self.value1 = value1
    self.value2 = value2

class EvenOrOdd(Number):
  def m(self):
    l_even = []
    l_odd = []
    if self.value1< self.value2 :
      for i in range (self.value1,self.value2+1):
        if i%2==0:
          l_even.append(i)
        else:
          l_odd.append(i)
    return l_even,l_odd
a1 = int(input("enter the starting number = "))
a2 = int(input("enter the ending number = "))    
b = EvenOrOdd(a1,a2) 
r = b.m()
print(r)
      
