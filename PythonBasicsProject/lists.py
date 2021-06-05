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
numbers = [1, 2, 3, 4, 5, 6, 5]
numbers.append(7)
numbers.insert(3, 2) # index, element
print("the list of numbers is : " + str(numbers))
numbers.remove(2) # 2 from the list
print("the updated list of numbers is : " + str(numbers))
print("pop", numbers.pop()) # removes the last element from the list
# Check existence/occurrence of an item in the list using index/in operator
print("Occurrence of a element 5 in list ", numbers.index(5))
# print("Occurrence of a element not exist in list ", numbers.index(50)) # Error not in the list
print("Occurrence of a element 5 in list ", 5 in numbers)
print("Count the Occurrences of a element 5 in list ", numbers.count(5))
print("Size of a list ", len(numbers)) # size of the list
numbers.sort() # sorting of the list, be default in ascending order, call reverse method to sort in descending
print("Sort the list in ascending by default ", numbers)
numbers.reverse()
print("Sort the list in descending ", numbers)
anotherList = numbers.copy()
print("Copy Method to copy the entire list ", anotherList)
numbers.clear() # clears everything from the list
print("final list of numbers: "+str(numbers))




