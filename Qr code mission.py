import NODE_ESPM as esp
from time import sleep

#Servo = esp.ESPM('192.168.43.84')  
#Servo.Close()

def fallow(path):
    #Fallow the path
    pass
def stopcenter(center):
    #turn camera down and go to center of qr
    pass

i = 0
foundqr = False
inmission = False
mistogo = [1,3,4]



while True:
    n = int(input("number"))
    QRs = ['E,W,N,S,'+str(n)]


    if len(QRs) > 0:
        Qr = QRs[0]
        center = (1,1)
        foundqr = True
        if inmission == False:
            name = Qr.split(',')  
        if inmission == False and int(name[4]) == 0:
            path = name[mistogo[i]-1]                
            stopcenter(center)
            fallow(path)
            print(path)
            
        elif inmission == False and int(name[4]) == mistogo[i]:
            inmission = True
            print("in mission",mistogo[i])

        if inmission == True:
            Misnum = mistogo[i]
            if Misnum == 1:
                #go to the center of the + and drop the box and stop mision and i = i + 1 
                #Servo.Open()
                #sleep(1)
                #Servo.Close()
                print("M1")
                sleep(1)
                i = i + 1
                inmission = False
                pass

            elif Misnum == 2:
                #go to the tower and read qr take pic and open loop and stop mision and i = i + 1
                print("M2")
                sleep(1)
                i = i + 1
                inmission = False
                pass

            elif Misnum == 3:
                #go to victims find qrs and take pic stop mision and i = i + 1 
                print("M3")
                sleep(1)
                i = i + 1
                inmission = False
                pass

            elif Misnum == 4:
                print("M4")
                sleep(1)
                i = i + 1
                inmission = False
                pass
            
