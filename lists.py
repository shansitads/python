kpop = ["NCT", "BTS", "Red Velvet", "Exo", "Stray Kids", "Red Velvet"] #you can put a variety of data types in one list
numbers = [4, 2, 7, 9, 0]
print(kpop)
print(kpop[0])
print(kpop[-1]) #indexing from the back
print(kpop[2:]) #index 2 ONWARDS TILL THE END
print(kpop[2:4]) #index 2 till 4-1=3 i.e. exclusive of upper bound 4

#list functions
print("\nLIST FUNCTIONS:")

print()
#sort
kpop.sort()
print("Ascending sort kpop list: " + str(kpop))
numbers.sort()
print("Ascending sort number list: " + str(numbers))
numbers.reverse()
print("Reverse number list: " + str(numbers))

print()
#length, index, count
print("Length of list: "+ str(len(kpop)))
print("Index of BTS: "+ str(kpop.index("BTS")))
print("Red Velvet is present " + str(kpop.count("Red Velvet")) + " times")
print("IU is present " + str(kpop.count("IU")) + " times")


print()
#add elements
kpop.append(numbers) #entire list of numbers is appended as a single element in kpop list
print("List after appending: " + str(kpop))
kpop.extend(numbers) #each element is separately added
print("List after extending: " + str(kpop))
kpop.insert(3, "Twice") #insert element at specified index
print("List after inserting: " + str(kpop))


print()
#remove/pop elements
kpop.remove(numbers) #removes by content of element, not by index
kpop.remove("Red Velvet") #even if element repeats in the list, it is only removed once
print("List after removing : " + str(kpop))
kpop.pop() # remove last element
print("List after popping  : " + str(kpop))

print()
#copy lists
kpop2 = kpop.copy()
print("Copy of kpop: " + str(kpop2))

kpop.clear()
