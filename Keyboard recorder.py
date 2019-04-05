import keyboard
from time import sleep    
import os
#####################################################################
#paths
datafile = ('Keyboard_recorder/data.txt')
#make data storage
if os.path.exists('Keyboard_recorder'):
    print("Data loaded succesfuly!\n")
else:
    print("Creating data storage...")
    os.makedirs('Keyboard_recorder',0o777)
    with open(datafile, "x") as maindata:
        pass
    print("Data storage created succesfuly!\n")
#####################################################################
def Options(X):
   #Record
    if X == 'start' or X == '1':
        inputs = keyboard.record(until ='Esc') 
        with open(datafile, "a") as maindata:
            line = '\n'+str(inputs)
            maindata.write(line)
   #Read all
    elif X == 'read all' or X == '2':
        with open(datafile, "r") as maindata: 
            data = maindata.read()
            print(data)
        print("")
        print("")
   #Read a recording
    elif X == 'read line' or X == '3':
        lines = 0
        with open(datafile, "r") as maindata:
            for line in maindata:
                lines = lines + 1
        print(lines)
        linen = int(input("Which line is it that you recall? "))
        print('')
        linecount = 0
        with open(datafile, "r") as maindata:
            for line in maindata:
                linecount = linecount + 1
                if linecount == linen:
                    target = line
        print(target)
        print("")
        print("")
#####################################################################
while True:
    print("!! Hello and welcome to keboard recorder !!")
    print("Option 1 or 'start': Starts recording")
    print("Option 2 or 'read': Shows the data stored")
    print("Option 3 or'read line': Shows the data stored on one line")
    print("")
    option = str(input("Waiting for input: "))
    print("")
    Options(option)