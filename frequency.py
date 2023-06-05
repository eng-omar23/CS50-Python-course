def calculate_total_frequency(lst):
    total_frequency = 0
    for number in lst:
        frequency = lst.count(number) / len(lst)
        total_frequency += frequency
    return total_frequency

# Test the function
my_list = [1, 2, 2, 3, 4, 2, 5, 5, 5]
result = calculate_total_frequency(my_list)
print("The total frequency of numbers in the list is:", result)
