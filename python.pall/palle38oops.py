class Doctor :
  def m1(self,doctor_name):
    print(f"hello {doctor_name}")

  def m2(self,doctor_name,specialist):
    print(f"{doctor_name} is {specialist}")

dr = Doctor()
dr.m1("Dr.Ramesh")
dr.m2("Dr.Ramesh","dentist")