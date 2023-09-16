import copy

original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)

shallow_copy[0] = 73  # This change won't affect the original list
shallow_copy[1][0] = 33  # This change will affect the original list

print(original_list)  # Output: [1, [6, 3], 4]
# print(shallow_copy)
