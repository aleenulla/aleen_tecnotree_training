# Ask the user to enter a list of numbers, separated by commas
numbers = input("Enter a list of numbers, separated by commas: ").split(",")
numbers = [int(num) for num in numbers]

# Use a for loop to iterate through the numbers in the list, and add up the even numbers
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num

# Print the result
print("The sum of all the even numbers in the list is:", even_sum)
