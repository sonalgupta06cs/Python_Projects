# find the largest number in a list
numbers = [3, 6, 11, 2, 8, 4, 10]
maxNum = numbers[0]
for number in numbers:
    if number > maxNum:
        maxNum = number
    else:
        continue
print("max number is ", maxNum)


# Remove the duplicates from the list - 1
numbersList1 = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
counter = 0;
for number in numbersList1:
    if number not in uniques:
        uniques.insert(counter, number)
        counter += 1
    else:
        continue
print("unique list of elements in the list 1 are ", uniques)


# Remove the duplicates from the list - 2
numbersList2 = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbersList2:
    if number not in uniques:
        uniques.append(number)
    else:
        continue
print("unique list of elements in the list 2 are ", uniques)





