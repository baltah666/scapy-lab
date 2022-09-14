import scapy.all as scapy
import socket
import os

juniper = ("0c:2f:0b:da:00:00" , "0c:a1:4b:2e:00:00")
#juniper = "0c:a1:4b:2e:00:00"
Extrem  = ("0c:a8:2b:6d:00:00","0c:ea:54:42:00:00","0c:a8:2b:6d:00:00")
cisco   = "9a:f2:07"


request = scapy.ARP()
#x = raw_input("Enter IP address: ")
x = "192.168.174.1/24"
request.pdst = x

broadcast = scapy.Ether()
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout = 1)[0]

print("***************************************************************************************************")
print("IP" + " "*25+"MAC"+" "*20+"ScannerIP"+ " "*14+"Vendor" + " "*14+"Hostname" )
print("***************************************************************************************************")
for element in clients:
	
	if element[1].hwsrc.startswith(juniper)== True:
		a = element[1].psrc
		b =  socket.gethostbyaddr (a)
		print(element[1].psrc + "        " + element[1].hwsrc +  "        " + element[1].pdst + "        " + "juniper" +  "                " +  str(b[0]) )

	if element[1].hwsrc.startswith(Extrem)== True:
                a = element[1].psrc
                b =  socket.gethostbyaddr (a)
	        print(element[1].psrc + "        " + element[1].hwsrc +  "        " + element[1].pdst + "        " + "Extrem"  +  "                " +  str(b[0]))

        if element[1].hwsrc.startswith(cisco)== True:
                a = element[1].psrc
                b =  socket.gethostbyaddr (a)
		print(element[1].psrc + "        " + element[1].hwsrc +  "        " + element[1].pdst + "        " + "cisco"   +  "                 " +  str(b[0]))
        	
#		else :
#		print(element[1].psrc + "        " + element[1].hwsrc +  "        " + element[1].pdst + "        " + "linux"   +  "                 " +  str(b[0]))

print(" ****************************************************************************************************")

