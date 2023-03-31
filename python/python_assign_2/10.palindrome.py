def find_palindromes(str_list):
    # Initialize an empty list
    palindromes = []

    # iterate each element
    for string in str_list:
        if string == string[::-1]:          #checking palindrome
            palindromes.append(string)      #add palidrome to list
    return palindromes


string_list = ["mom", "hello", "level", "world", "bus"]
palindromes = find_palindromes(string_list)
print(palindromes)

