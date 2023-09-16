# def age (x):
#   if x >= 18 and x < 20:
#     return "child"
#   elif x >= 20 and x<=50 :
#     return "adult"
#   elif x>=51:
#     return "senior citizen"
#   else:
#     return "not proper responce "
# a = age(int(input("enter the age of the candidate here: ")))    
# print(a)

age = lambda x: "child" if x >= 18 and x < 20 else "adult" if x >= 20 and x <= 50 else "senior citizen" if x >= 51 else "not proper response"
print(age(int(input("enter the age to check the category here : "))))