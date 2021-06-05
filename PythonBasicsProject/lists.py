# Tuples are like lists, but they are immutable
#tuples_lists = (1, 2, 3)
# [0] = 10 # error cant be changes as it is immutable
#tuples_lists.count(1)
#tuples_lists.index() # returns the index of the elements


# Lists, a list of elementsround
print("----------List Method Operations-----------------")
names = ["John", "Bob", "Mosh", "Sam", "Marry"]
print("names: "+str(names))
print("the element in list: "+str(names[0])) # 0 index represents the first element in the list
print("the last element in the list: "+str(names[-1])) # -1 represents the last element in the list, -2 second last.
names[0] = "Jon"
print("updated list elements: " + str(names))
print("selected number of elements: " + str(names[0:3])) # last index is excluding the elements, it returns a new list


##############################################
# List Methods, string in python are objects, list are also objects, so they also have objects
numbers = [1, 2, 3, 4, 5, 6]
numbers.append(7)
numbers.insert(3, 2) # index, element
print("the list of numbers is : " + str(numbers))
numbers.remove(2) # 2 from the list
print("the updated list of numbers is : " + str(numbers))
print(1 in numbers)
print(len(numbers)) # size of the list
numbers.clear() # clears everything from the list
print("final list of numbers: "+str(numbers))




