# find the largest number in a list
numbers = [3, 6, 11, 2, 8, 4, 10]
maxNum = numbers[0]
for number in numbers:
    if number > maxNum:
        maxNum = number
    else:
        continue
print("max number is ", maxNum)

