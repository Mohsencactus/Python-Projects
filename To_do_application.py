import os
#from time import sleep

#paths
datafile = ("Todo data/data.txt")
taskfile = ("Todo data/task.txt")
weekdays = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']

#make data storage
if os.path.exists('Todo data'):
    print("Data loaded succesfuly!\n")
else:
    print("Creating data storage...")
    os.makedirs('Todo data',0o777)
    tasks = ['','','','','','','']
    with open(taskfile, "x") as maintask:
        for g in range(len(tasks)):
            line = tasks[g]+'\n'
            maintask.write(line)
    with open(datafile, "x") as maindata:
        for i in range(len(weekdays)):
            line = weekdays[i]+': '+'\n'
            maindata.write(line)
    print("Data storage created succesfuly!\n")



#options and all
def options(X):
   #Show the week days plus their tasks
    if X == 1:
        #showing the whole file
        with open(datafile, "r") as maindata: 
            data = maindata.read()
            print(data)

   #Show a specific day of the week plus its task
    elif X == 2:
        day = int(input("Which day is it that you recall? "))
        print('')
        daycount = 0
        #showing line
        with open(datafile, "r") as maindata:
            for line in maindata:
                daycount = daycount+ 1
                if daycount == day:
                    print(line)

   #Asign a task to a specific day
    elif X == 3:
        #reading from the task file that was saved
        with open(taskfile, "r") as maintask:
            tasks = []
            for line in maintask:
                line = line.replace('\n', '')
                tasks.append(line)
        task = str(input("What is it that you want to do on that day? "))
        daynum = int(input("What day should it be on? "))
        print('')
        tasks[daynum-1] = task
        #writing the tasks to the task file
        with open(taskfile, "w") as maintask:
            for f in range(len(tasks)):
                line = tasks[f]+'\n'
                maintask.write(line)
        #writing to the list
        with open(datafile, "w") as maindata:
            for j in range(len(weekdays)):
                line = weekdays[j]+': '+str(tasks[j])+'\n'
                maindata.write(line)
   #RESETING 
    elif X == 4:
        #reading from the task file that was saved
        with open(taskfile, "r") as maintask:
            tasks = []
            for line in maintask:
                line = line.replace('\n', '')
                tasks.append(line)
        tasks = ['','','','','','','']
        #writing the tasks to the task file
        with open(taskfile, "w") as maintask:
            for f in range(len(tasks)):
                line = tasks[f]+'\n'
                maintask.write(line)
        #writing to the list
        with open(datafile, "w") as maindata:
            for j in range(len(weekdays)):
                line = weekdays[j]+': '+str(tasks[j])+'\n'
                maindata.write(line)

  #sleep(2)

while True:
    print("You have started the 'To Do' aplication")
    print("From the options below choose what you want to do")
    print("Note! In choosing days and options use numbers!!")
    print("Option #1: Show the week days plus their tasks")
    print("Option #2: Show a specific day of the week plus its task")
    print("Option #3: Asign a task to a specific day")
    print("Option #4: Reset all the tasks assigned")
    option = int(input("Please choose the number of option: "))
    print('')
    options(option)