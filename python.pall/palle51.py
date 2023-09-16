def min_number_operations(target, size):
    total_moves = 0
    initial_array = [0] * size
    
    for i in range(size):
        diff = target[i] - initial_array[i]
        total_moves += diff
        
        # Update the initial array to match the target array
        for j in range(i, size):
            initial_array[j] += diff
    
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
