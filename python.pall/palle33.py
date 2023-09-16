l = [1,2,3,4,5]

for i in range(len(l)):
    total = 1
    for j in range(len(l)):
        if j != i:
            total *= l[j]
    print(f"For {i+1}st index position - {total}")
