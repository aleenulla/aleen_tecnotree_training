
list1 = [8, 3, 1, 12, 6]
list2 = [23, 5, 6, 9, 12]


same_elemts = []  

for element in list1: # iterating each element 
    if element in list2:
        same_elemts.append(element) #appending the elemt into samw_elemts

print("Elements that appear in both lists are:", same_elemts)
