def dictionary(X):
    var = {"root": 123456,"usr1": "password","usr2": "mozlover","usr3":654321}

    #show the whole dict
    if X == 1:
        print(var)

    #show a specific house
    elif X == 2:
        a = var["root"]
        print(a)
    
    #change a specific house
    elif X == 3:
        var["usr3"] = 123456
        print(var)
    
    #show all the houses id's
    elif X == 4:
        for a in var:
            print(a)
    
    #show the houses values in two ways
    elif X == 5:
        #first way
        print("first way: ")
        for a in var:
            vall = var[a]
            print(vall)
        print("")  
        #second way
        print("second way: ")
        for a in var.values():
            print(a)  
    
    #show houses with their values
    elif X == 6:
        for a,b in var.items():
            c = (a,b)
            print(c,a,b)

    #check if a specific house exist
    elif X == 7:
        a = input("whats the username? ")
        if a in var:
            print("Yes")
        else :
            print("No")

    #add a house to the dict
    elif X == 8:
        a = input("whats the username? ")
        b = input("whats the password? ")
        var[a] = b
        print(var)
    
    #remove a house
    elif X == 9:
        a = input("whats the username which u like to remove? ")
        var.pop(a)
        print(var)


    #remove all the houses
    elif X == 10:
        var.clear()
        print(var)
    
    #make a dict
    elif X == 11:
        var2 = dict(usr1=123456, usr2=654321, usr3="password")
        print(var2)

while True:
    print("")
    X = int(input("choose the number u want: "))
    print("")
    dictionary(X)
    
