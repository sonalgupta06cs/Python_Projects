# While Loops, can have 1_000 instead of 1000 to make it more readable
wi = 1
while wi <= 10:
    print(wi * '*')
    wi += 1

print("-----------ForWhileLoop----------------")
# For Loops
nums = [1, 2, 3, 4, 5]
for item in nums:
    print(item)

i = 0
while i < len(nums):
    print(nums[i])
    i += 1

print("-----------Range Function with for/while----------------")
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

# Nested Loops
print("----------Nested Loops-----------------")
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

