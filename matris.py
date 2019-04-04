def matris(O,Xin,Yin):
    
    if O == 1:
        for Y in range(1,Yin+1):
            for X in range(1,Xin+1):
                for Z in range(1,Y):
                    print(X,'',end='')
                print("")
            print("")
   
    elif O == 2:
        for Y in range(1,Yin+1):
            for X in range(1,Xin+1):
                print(X*Y,'',end='')
            print("")

    elif O == 3:
        for X in range(1,Xin+1):
            for Z in range(0,X):
                print(X,'',end='')
            print("")
        

    elif O == 4:
        for X in range(1,Xin+1):
            space = ' '
            Z = Xin - X
            print(space*Z,end='')
            for Z in range(0,X):
                print(X,'',end='')
            print("")

    elif O == 5:
        pass

while True:
    Xin = int(input("Number X is: "))
    Yin = int(input("Number Y is: "))
    O = int(input("Type of matris: "))
    matris(O,Xin,Yin)