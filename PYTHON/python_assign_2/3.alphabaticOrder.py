cars = ["volvo", "mercedes", "tata", "Audi", "kia"]

sorted_strings = [] # empty list 
for string in cars: #iterting each elemet
    for i in range(len(sorted_strings)):
        if string < sorted_strings[i]:
            sorted_strings.insert(i, string)
            break
    else:
        sorted_strings.append(string)

# Print the sorted list of strings
print("Sorted list of strings:", sorted_strings)
