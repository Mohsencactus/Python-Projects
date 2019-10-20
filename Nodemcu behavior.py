import NODE_ESPM as esp

Servo = esp.ESPM('192.168.43.84')

while True:
    X = input("Should I open or close? ")
    X = X.upper()
    if X == 'OPEN':
        Servo.Open()
    elif X == 'CLOSE':
        Servo.Close()