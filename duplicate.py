def remove_duplicates(lst):
    return list(set(lst))

# Test the function
my_list = [1, 2, 2, 3, 4, 2, 5, 5, 5]
result = remove_duplicates(my_list)
print("List after removing duplicates:", result)
