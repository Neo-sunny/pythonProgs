"""
Solution - Analyze a reference issue involving a nested list
"""

# Create a nested list
zero_list = [0, 2, 0]
nested_list = []
for dummy_idx in range(5):
    nested_list.append(zero_list)
print(nested_list)

# Update an entry to be non-zero
nested_list[0] = 7
print(nested_list)




# Erroneous output
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
#[[0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0]]

# Desired output
# [[0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0]]
# [[0, 2, 0], [0, 2, 0], [0, 7, 0], [0, 2, 0], [0, 2, 0]]


# Explanation
