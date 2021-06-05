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