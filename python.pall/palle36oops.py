class Employee:
  def __init__(self,name , age ,phone_number , address ):
    self.name = name
    self.age = age 
    self.phone_number = phone_number
    self.address = address 

  def greet(self):
    print(f"hello {self.name}\n")
    print(f"The name of the employee is {self.name}\n")
    print(f"The age of the employee is {self.age}\n")
    print(f"You can contact the employee at {self.phone_number}\n")
    print(f"The address of the employee is {self.address}")


cadet_1 = Employee("Tarun", 34, "932413123", "Guljarpura")
cadet_2 = Employee("Ramesh", 23, "9235131313", "Radhenagar")

cadet_1.greet()
cadet_2.greet()