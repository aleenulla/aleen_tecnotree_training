#list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0 #initialize the variablw into zero

for num in numbers: # check each element
    if num % 2 == 0:
        even_sum =even_sum+num

print("Sum of even numbers in the list is:", even_sum)
