#!/bin/python3

import sys #allows us to enter command line arguments, among other targets
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate host name to IPV4
else:
    print("Invalid amount of arguments.")
    print("Syntax:python3 Scaner.py <IP>")
    sys.exit()

#Add a banner
print("-" * 50)
print("Scanning target: "+ target)
print("Timestarted: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET is ipv4  and SOCK_STREAM is my port
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #return error indicator
        print("checking port {}".format(port))
        if result == 0:
            print("port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror: #we cannot connect to host name
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("coundn't connect  to server.")
    sys.exit()
