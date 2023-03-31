# Take input from user
string = input("Enter a string: ")
letter_count = {}

for char in string:
    if char.isalpha(): #true
        if char in letter_count:
            letter_count[char] += 1  #increment the value 
        else:
            letter_count[char] = 1 #initializing to one when it appears first

print("Letter count:", letter_count)
