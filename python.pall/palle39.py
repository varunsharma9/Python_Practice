print("first project")
def hospital(name , bg ,*disease ,email ='email is not given'):
  print(name)
  print(bg)
  print(disease)
  print(email)
hospital("varun","B+","psycology","artis","headache",email="gggg@gmail.com")

print("//////////////////////////////////////////////////////////////////////////////////////////////")

print("seconf project")
def training_institute(name ,*email,**add):
  print(name)
  print(email)
  print(add)
training_institute("varun","a@gmail.com","b@gmail.com","c@gmail.com",country ='india',state = 'maha',city='Akola') 