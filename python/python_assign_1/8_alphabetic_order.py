names = input("Enter a list of names, separated by commas: ").split(",")
names = [name.strip() for name in names] # Remove any leading or trailing whitespace

# Sort the names in alphabetical order
names_sorted = sorted(names)

# Print the results
print("The names in alphabetical order are:")
for name in names_sorted:
    print(name)
