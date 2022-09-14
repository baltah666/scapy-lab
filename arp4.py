import scapy.all as scapy
import socket
import os

request = scapy.ARP()
#x = raw_input("Enter IP address: ")
x = "192.168.174.1/24"
request.pdst = x

broadcast = scapy.Ether()
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout = 1)[0]
os.system('clear')
print (clients)
print(" ************************************************************************************")
print("IP" + " "*20+"MAC"+" "*20+"scanner"+" "*15+"hostname")
print(" *************************************************************************************")

for element in clients:
	a = element[1].psrc
#        y= "192.168.174.250"
#        b =  socket.gethostbyaddr (y)
        b =  socket.gethostbyaddr (a)
#	print(element[1].psrc + "	 " + element[1].hwsrc +  "        " + element[1].pdst + "          " +  a)
	print(element[1].psrc + "	 " + element[1].hwsrc +  "        " + element[1].pdst + "          " +  str(b[0]))
#print(type(a))
#print(type(b))
#print(type(x))
#        p=(element[1].psrc)
#        print(p)
#        if p == "0c:9f:2d:e4:00:00"
#           then print("Juniper")
print(" *************************************************************************************\n")
print(" *************************************************************************************\n")

