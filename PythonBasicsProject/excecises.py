# Type Conversion: Exercise first 10.1, second 20, sum 30.1
first = input("Enter First: ")
second = input("Enter Second: ")
sumResult = float(first) + float(second)
print('The sum is: ' + str(sumResult))

# Weight: 170
# (K)g or (L)bs : l
# Weight in Kg: 76.5
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
birth_year = input("Enter your birth year: ")
print(type(birth_year))
age_user = 2021 - int(birth_year)
print(type(age_user))
print("Your age is: ", age_user)

# String in multiple lines
course = '''
Hi John,

Here is our first email to you !

Thanks,
The Support Team
'''
print(course)

# Accessing the elements in String
learning_language = 'Javas'
print(learning_language[0] +", " + learning_language[-1])
print(learning_language[0:3])
print(learning_language[0:])
print(learning_language[1:])
print(learning_language[:5])
print(learning_language[:])

#
print("---------------------------")
name = 'Jennifer'
print("name:- " + name[1:-1])

