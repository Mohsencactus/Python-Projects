while True:
    number = input("Enter the number please: ")

    rghm = len(number)
    adad = int(number)
    ints = []
    finals = []

    for i in range (1,rghm+1):
        zrib = 10**(rghm-i)
        add = int(adad/zrib)
        ints.append(add)
        if i == 1:
            finals.append(add)
        else:
            extract = int((add/10-(ints[i-2])+0.01)*10)
            finals.append(extract)

    for g in range (1,len(finals)+1):
        smt = len(finals) - g
        print(finals[smt],end ='')
    print("")