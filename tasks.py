# 2.4 Python

# Create good script to create new list, which only contains users from Poland. Try to do it with List Comprehension:

users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}]
poland_users = [item for item in users if item.get("country") == "Poland"]
print(poland_users)


# Display sum of first ten elements starting from element 5:

numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]
sum_of_first_ten = sum(numbers[4:14])
print(sum_of_first_ten)


# Fill list with powers of 2, n [1..20]:

powers_of_2 = [2 ** i for i in range(1, 21)]
print(powers_of_2)
