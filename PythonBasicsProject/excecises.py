# Type Conversion: Exercise first 10.1, second 20, sum 30.1
print("---------Calculate Sum------------------")
first = input("Enter First: ")
second = input("Enter Second: ")
sumResult = float(first) + float(second)
print('The sum is: ' + str(sumResult))

# Weight: 170
# (K)g or (L)bs : l
# Weight in Kg: 76.5
print("---------Convert weight------------------")
weight = int(input("Enter Weight: "))
unit = input("K(g) or (L)bs: ")
if unit.upper() == 'K':
    weightLb = weight / 0.45
    print("Weight in Lbs: "+str(weightLb))
else:
    weightKg = weight * 0.45
    print("Weight in Kg: "+str(weightKg))


# Type Conversion from 1 type to another => int() method, float(), bool(), str()
# input function would always return a value as string as "1989" so 2021 - "1989"(birth_year)
print("---------Calculate Age------------------")
birth_year = input("Enter your birth year: ")
print(type(birth_year))
age_user = 2021 - int(birth_year)
print(type(age_user))
print("Your age is: ", age_user)

# String in multiple lines
print("---------String Multiple Lines------------------")
course = '''
Hi John,

Here is our first email to you !

Thanks,
The Support Team
'''
print(course)

print("---------AccessStringElements------------------")
# Accessing the elements in String
learning_language = 'Javas'
print(learning_language[0] +", " + learning_language[-1])
print(learning_language[0:3])
print(learning_language[0:])
print(learning_language[1:])
print(learning_language[:5])
print(learning_language[:])


name = 'Jennifer'
print("name:- " + name[1:-1])

print("-----------ForLoopExercise----------------")
# add the price and sum the total amount
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f'total is {total}')

print("----------ForLoopExerciseToPrint'F'-----------------")
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print(number * "*")

print("----------NestedLoopExerciseToPrint'F'-----------------")
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ""
    for y_count in range(x_count):
        output += "*"
    print(output)

print("----------NestedLoopExerciseToPrint'L'-----------------")
numbers = [1, 1, 1, 1, 5]
for x_count in numbers:
    output = ""
    for y_count in range(x_count):
        output += "*"
    print(output)