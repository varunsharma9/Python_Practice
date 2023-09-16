def min_number_operations(target, size):
    total_moves = 0
    for i in range(size):
        diff = target[i] - total_moves
        total_moves += diff
        
    return total_moves

# Example 1
target1 = [3, 1, 1, 2]
size1 = 4
output1 = min_number_operations(target1, size1)
print(output1)  # Output should be 4

# Example 2
target2 = [3, 1, 5, 4, 2]
size2 = 5
output2 = min_number_operations(target2, size2)
print(output2)  # Output should be 7
