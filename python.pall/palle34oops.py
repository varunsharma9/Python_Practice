class Student:
  name = 'Ram'
  age = 22
  place = 'Banglore'
  
  def study(self,subject):
    print(f"the Ram is studying {subject}")
s1 = Student()
print(s1.name)
s1.study('python')