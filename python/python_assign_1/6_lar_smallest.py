nums = input("Enter a list of numbers, separated by commas: ").split(",")
nums = [float(num) for num in nums] # Convert the input string to a list of floats

# Find the largest and smallest numbers in the list
largest = max(nums)
smallest = min(nums)

# Print the results
print(f"The largest number in the list is {largest}")
print(f"The smallest number in the list is {smallest}")
