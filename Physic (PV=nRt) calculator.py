R  = 8
P = input("Enter 'P' value: ")
V = input("Enter 'V' value: ")
n = input("Enter 'n' value: ")
T = input("Enter 'T' value: ")
print('')
Values = [P,V,n,T]

for b in range (len(Values)):
    if Values[b] == '':
        X = b
        continue
    Values[b] = int(Values[b])

P,V,n,T = Values 
try:
    #P is unknown
    if X == 0:
        Result = (n*R*T)/V
        Label = "'P'"
    #V is unknown
    elif X == 1:
        Result = (n*R*T)/P
        Label = "'V'"
    #n is unknown
    elif X == 2:
        Result = (P*V)/(R*T)
        Label = "'n'"
    #T is unknown
    elif X == 3:
        Result = (P*V)/(R*n)
        Label = "'T'"

    print(Label + ' is:',Result)
except:
    print("All values are known. Solve it Your self")