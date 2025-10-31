# a = ("Monday","tuesday")
# news_day = ("funday",)+a
# print(news_day)

# user_input = input()

# languages = tuple(user_input.split(","))

# new_language = input()

# updated_languages = languages + (new_language,)

# print("Updated Tuple:", updated_languages)
# Let's create a tuple with numbers
# my_tuple = (1, 2, 3, 4, 5)

# # Now, let's iterate through the tuple using a for loop
# # The loop retrieves each number in the tuple and prints it
# for number in my_tuple:
#     print(number)  # Outputs: 1 2 3 4 5

# # Collecting user input as a string of vegetables separated by commas
# user_input = input()

# # Converting user input to a tuple of vegetables
# vegetables = tuple(user_input.split(','))

# # Iterate through the vegetables tuple and print each vegetable
# print(vegetables)
# for vegetable in vegetables:
#     # Print the vegetable's name here
#     print(vegetable)

# Step 1: Take user input for the tuple elements
# user_input = input( ).strip()

# # Step 2: Convert input into a tuple (removing extra spaces for each element)
# user_tuple = tuple(value.strip() for value in user_input.split(","))

# # Step 3: Take user input for the element to count
# search_element = input( ).strip()

# # Step 4: Count occurrences of the search element in the tuple
# count_result = user_tuple.count(search_element)

# # Step 5: Print the result
# print(f"The element '{search_element}' appears {count_result} time(s) in the tuple.")

# Define a tuple with various elements
# Step 1: Predefine a tuple of popular tourist destinations
# cities = ("Paris", "Tokyo", "New York", "London", "Dubai", "Rome", "Sydney","Tokyo")

# # Step 2: Take user input for a city name
# search_city = input().strip()

# # Step 3: Check if the city is in the tuple
# if search_city in cities:
#     city_index = cities.index(search_city)  # Get the index of the city
#     print(f"The city '{search_city}' is found at index {city_index}.")
# else:
#     print("City not found.")

# Step 1: Take user input for javelin throw distances
# user_input = input().strip()

# # Step 2: Convert input into a tuple of floats (removing extra spaces for each value)
# throw_distances = tuple(float(value.strip())for value in user_input.split(","))

# # Step 3: Find the total number of participants
# num_participants = len(throw_distances)

# # Step 4: Determine the shortest and longest throws
# shortest_throw = min(throw_distances)
# longest_throw = max(throw_distances)

# # Step 5: Calculate the total sum of all throws
# total_distance = sum(throw_distances)

# # Step 6: Print the results
# print(f"Total number of participants: {num_participants}")
# print(f"Longest throw: {longest_throw} meters")
# print(f"Shortest throw: {shortest_throw} meters")
# print(f"Total sum of throws: {total_distance} meters")

# n = int(input())
# # cook your dish here
# for i in range(1, n + 1):
#     # Inner loop to print numbers in the current row
#     for j in range(1, i + 1):
#         # Check if it's the first column in the row
#         if j == 1:
#             print(1, end=" ")  # Print 1 for the first column
#         # Check if it's the last column in the row
#         elif j == i:
#             print(i, end=" ")  # Print the row number (i) for the last column
#         else:
#             print(0, end=" ")  # Print 0 for all intermediate columns
#     print()  # Move to the next line after completing the current row


# def increment(number):
#     number += 1  # Tries to modify the local variable 'number'
#     return number

# # Initial number
# my_number = 5
# a=increment(my_number)  # Function does not modify the original number
# print(a)  # Outputs: 5 - The original number remains unchanged
# Function to add two numbers
def add(x, y):
    return x + y

# Function to multiply two numbers


def multiply(x, y):
    return x * y

# Function that takes an operation (another function) and applies it to two numbers


def calculate(operation, a, b):
    # Calls the function passed as 'operation' with a and b
    return operation(a, b)


# Using 'calculate' with different operations
result1 = calculate(add, 5, 3)        # Calls add(5, 3) -> 8
result2 = calculate(multiply, 5, 3)   # Calls multiply(5, 3) -> 15

# Printing the results
print(result1)  # Output: 8
print(result2)  # Output: 15
