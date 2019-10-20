import os

root_url = "http://192.168.43.84" #+input("Enter IP: ")

def sendRequest(url):
	os.system('wget -t 1 '+ str(url))


while True:
	answer = input(""" To control theOn led, type "ON" or "OFF": """)
	if (answer=="on"):
		print(root_url+"/OPEN")
		sendRequest(root_url+"/OPEN")
		print("Opened!\n\n")
	elif (answer=="off"):
		print(root_url+"/CLOSE")
		sendRequest(root_url+"/CLOSE")
		print("Closed!\n\n")
