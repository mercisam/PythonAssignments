#create an empty list
my_list=[]
print("my empty list:",my_list)

#append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("list after append:",my_list)

#Insert the value 15 at the second position in the list.
my_list.insert(1,15)
print("After Inserting 15 at index 1:", my_list)

#extend my_list with another list
my_list2=[50,60,70]
print("list2:", my_list2)
#join two lists
my_list.extend(my_list2)
print("list after extend:",my_list)

#Remove the last element from my_list
del my_list[-1]
print("List after removing the last element:",my_list)

#sorting my_list in ascending order
my_list.sort()
print("list in ascending order:",my_list)
#Find and print the index of the value 30 in my_list.
my_list.index(30)
print("Index of value 30:",my_list.index(30))