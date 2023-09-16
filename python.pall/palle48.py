fruits = ['apple', 'banana', 'cherry', 'date']
filtered_dict = {fruit: len(fruit) for fruit in fruits if 'a' in fruit}
print(filtered_dict)  # Output: {'apple': 5, 'banana': 6}
