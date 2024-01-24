input = [[1, 2, 3], [2, 4, 1, 0]]

# Calculate the sum of the second-largest number in each sub-list
sum_second_largest = sum([sorted(sublist)[-2] for sublist in input])

print("Sum of the second-largest numbers:", sum_second_largest)

