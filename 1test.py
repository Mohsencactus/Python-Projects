Xin = int(input("Number X is: "))
Yin = int(input("Number Y is: "))

for Y in range(1,Yin+1):
    for X in range(1,Xin+1):
        for Z in range(1,Y):
            print(X,'',end='')
        print("")
    print("")