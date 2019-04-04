import random as rd

def dice():
    number = rd.randint(1,6)
    return number

def options(X):
   #If you want to bet get the bet
    if X == 'Y' or X == 'y' or X == 'YES' or X == 'yes' or X == '1' or X == 'Yes':
        print("")
        bet = int(input("Whats the number your betting on?: "))
        input("!!!!!! HIT ENTER ON KEYBOARD TO ROLL THE DICE !!!!!!")
        print("")
        luck = dice()
        if bet == luck:
            print("")
            print("!!! YOU WON !!!")
            print('Your number is: '+str(luck))
            print("")
        else:
            print("")
            print("! YOU LOSE!")
            print('Your number is: '+str(luck))
            print("")
   #If not just roll
    else:
        print("")
        input("!!!!!! HIT ENTER ON KEYBOARD TO ROLL THE DICE !!!!!!")
        print("")
        luck = dice()
        print('Your luck is: '+str(luck))
        print("")

while True:
    print("")
    option = str(input("Do you want to guess your luck? "))
    print("")
    options(option)



