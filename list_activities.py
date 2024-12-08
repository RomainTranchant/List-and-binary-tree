# Romain Tranchant
# CIS 103 Fundamentals of Programming
# Instructor: MD Ali
# List Activities

# Basic Operations

# Create a list from 1 to 10
my_list = list(range(1, 11))

# Print the initial list
print("My list:", my_list)

# Insert 11 at the 5th position (index 4)
# my_list.insert(4, 11)
my_list[4] = 11
# Print the list after insertion
print("\nThe list after insertion of 11 at the 5th position:", my_list)

# Remove the number 4 from the list
my_list.remove(4)
# Print the list after deletion
print("\nThe list after deletion of the number 4:", my_list)

# Print the list items in reversed order
print("\nAfter Traversal:")
for item in reversed(my_list):
    print(item, end=" ")

# Additional challenges

# Define a function to find the second largest number in the list
def find_second_largest(my_list):
# Remove duplicates by converting to a set and back to a list
    unique_lst = list(set(my_list))
# Sort the list in ascending order
    unique_lst.sort()
# Return the second largest number if there are at least two unique numbers
    return unique_lst[-2] if len(unique_lst) > 1 else None

# Define a function to sort the list in descending order
def custom_sort_desc(my_list):
# Iterate through the list
    for i in range(len(my_list)):
# Compare each element with the elements after it
        for j in range(i + 1, len(my_list)):
# Swap elements to sort in descending order
            if my_list[i] < my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
# Return the sorted list
    return my_list

# Define a function to search for a number in the list and return its index
def search_number(my_list, num):
# Iterate through the list with index and value
    for index, value in enumerate(my_list):
# Return the index if the number is found
        if value == num:
            return index
# Return -1 if the number is not found
    return -1

# Print the second largest number in the list
print("\n\nThe second largest number is:", find_second_largest(my_list))
# Print the list sorted in descending order
print("\nThe list in descending order is:", custom_sort_desc(my_list))
# Print the index of the number 3 in the list
print("\nSearching for the number 3 and printing the index:", search_number(my_list, 3))
