
days = ["monday", "tuesday", "wednesday", "thusday", "friday"]

longest_word = ""  #empty string

for word in days:
    if len(word) > len(longest_word):  # comparing the lngth of word
        longest_word = word
print("Longest word is:", longest_word)
