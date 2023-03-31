string = input("Enter a string: ")

# calculate the length of the string
length = len(string)

# get the first and last characters of the string
first_char = string[0]
last_char = string[length - 1]

# reverse the string
reverse_string = string[::-1]

print(f"The length of the string is {length}")
print(f"The first character of the string is {first_char}")
print(f"The last character of the string is {last_char}")
print(f"The string in reverse order is {reverse_string}")
