import random as rd 

while True:
    side = input("Welcome! Pick your side: 'X' or 'O'? ")
    if side == 'X' or 'x':
        ourside = 'O'
        break
    elif side == 'O' or 'o':
        ourside = 'X'
        break
    else:
        pass

print(ourside)