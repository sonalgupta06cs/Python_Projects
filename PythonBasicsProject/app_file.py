print('Sonal Gupta')

# variables
age = 32
print('age', age)
is_married = True
print('is_married', is_married)
spouse_name = 'Sachin Gupta'
print('spouse_name', spouse_name)

# Receiving Input from user from Terminal
profession = input("Enter your profession? ")
print("Hello, Your Profession " + profession + " seems great !")

# Type Conversion from 1 type to another => int() method, float(), bool(), str()
# input function would always return a value as string as "1989" so 2021 - "1989"(birth_year)
birth_year = input("Enter your birth year: ")
age_user = 2021 - int(birth_year)
print("Your age is: ", age_user)

# Strings Methods upper(), lower(), replace(x,y), find(x), "in" Operator as more user readable
course = 'Learning Python Now'
print(course.upper()) # does not change the original string, rather gives us a new string
print("Python" in course)

# Arithmetic Operators => +, -, *,, % Division:- / -> result with decimal, // -> only whole number
print(10 + 3)  # -> 13
print(10 / 3)  # -> 3.333333
print(10 // 3) # -> 3 , Another division operator
print(10 % 3)  # -> 1
print(10 ** 3) # -> 1000, Exponent Operator

# Augmented Assignment Operator => +=, -+, *=
aao = 10
aao += 3
print("aao: "+str(aao))

# Operator Precedence => * and / have higher precedence, so that part would be evaluated first.
# Exponentiation 2 ** 3
# Multiplication or Division
# Addition or Subtraction
y = 10 + 3 * 2    # -> 16
z = (10 + 3) * 2  # -> 26
s = 10 + 3 * 2 ** 2 # => 22
t = (2 + 3) * 10 - 3 # => 47

# Comparison Operators -> >, >=, <, <=, ==, !=
co = 3 > 2
print("CO: "+str(co))

# Logical Operators -> and, or, not
lo_price = 25
isPriceBetween = lo_price > 10 and lo_price < 30
print("lo isPriceBetween "+str(isPriceBetween))
print(not lo_price > 30)

# If  -> to get rid of block of code which gets executed, press shift + tab
# we have indentation to represent the block of code
temperature = 20
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20,30)
    print("It's a nice day")
elif temperature > 10: # (10,20)
    print("It's a bit cold")
else:
    print("It's cold")

# While Loops, can have 1_000 instead of 1000 to make it more readable
wi = 1
while wi <= 10:
    print(wi * '*')
    wi += 1

# Lists, a list of elementsround
names = ["John", "Bob", "Mosh", "Sam", "Marry"]
print("names: "+str(names))
print("the element in list: "+str(names[0])) # 0 index represents the first element in the list
print("the last element in the list: "+str(names[-1])) # -1 represents the last element in the list, -2 second last.
names[0] = "Jon"
print("updated list elements: " + str(names))
print("selected number of elements: " + str(names[0:3])) # last index is excluding the elements, it returns a new list


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


# For Loops
nums = [1, 2, 3, 4, 5]
for item in nums:
    print(item)

i = 0
while i < len(nums):
    print(nums[i])
    i += 1


# The range() Function is used to generate the sequence of numbers
gen_numbers = range(5) # range(5, 10) gen_numbers is a obj while will have numbers but excluding 5
print("gen_numbers: " + str(gen_numbers))

for num in gen_numbers:
    print(num)

print("*************")

for num in range(5, 10, 2):
    print(num)

for item in 'Python':
    print(item)



# Tuples are like lists, but they are immutable
tuples_lists = (1, 2, 3)
# [0] = 10 # error cant be changes as it is immutable
tuples_lists.count(1)
tuples_lists.index() # returns the index of the elements































