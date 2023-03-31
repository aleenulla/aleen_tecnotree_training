input_string = "Hello, World!"
vowels = "aeiouAEIOU"
new_string = ""   #empty list
for char in input_string:   #itearting each element
    if char not in vowels:
        new_string += char

print("The given string is : ",input_string)
print("The vowels are : ",new_string)  