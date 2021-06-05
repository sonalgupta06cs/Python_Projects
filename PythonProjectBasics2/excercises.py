##############################################

weight_lbs = input("Enter your weight in pounds :- ")
weight_kgs = int(weight_lbs) * 0.45
print('weight in kgs ' + str(weight_kgs))

##############################################
# House value to put down by x%
price_house = 1000000
has_good_credits = True
if has_good_credits:
    down_payment = 0.1 * price_house
else:
    down_payment = 0.2 * price_house
print("The down payment needs to be made for : ", f'Down payment: $ {down_payment}')

##############################################
# Guessing Game, secret number set to 9
secret_no = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_no:
        print("You won!")
        break
else: # else block for while, in python we can have else for while loop after while loop runs
      # successfully, it gets executed.
    print("Sorry, You Failed!")


##############################################
# Car Game
command = ""
isCarStarted = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if isCarStarted:
            print("Car is already started!")
        else:
            isCarStarted = True
            print("Car Started, Ready to go!")
    elif command == 'stop':
        if not isCarStarted:
            print("Car is already stopped.")
        else:
            isCarStarted = False
            print("Car Stopped.")
    elif command == 'help':
        print('''start - to start the car        
stop - to stop the car
quit - to quit the car''')
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that!")

##############################################
