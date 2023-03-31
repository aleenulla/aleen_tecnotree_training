# Take input from user
num_list = input("Enter a list of numbers : ")

# Convert the input string to a list 
squared_list = [int(num)**2 for num in num_list.split()]

# Print the squared list
print("Squared list:", squared_list)
