
# def booli(x):
#   for i in x:
#     if i % 2 == 0:
#       print("true")
#     else:
#       print("false")

# booli([23, 12, 37, 45, 34, 56])

num = lambda x : ["True" if i % 2 == 0 else "False" for i in x ]
result = num([23, 12, 37, 45, 34, 56])
print(result)