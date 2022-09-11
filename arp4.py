import scapy.all as scapy

request = scapy.ARP()
x = raw_input("Enter IP address: ")
request.pdst = x

broadcast = scapy.Ether()
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout = 1)[0]
print (clients)
print(" ***************IP Node Live*****************\n")
print("IP" + " "*20+"MAC"+" "*20+"sender")
for element in clients:
	print(element[1].psrc + "	 " + element[1].hwsrc +  "        " + element[1].pdst)
#        print("")
#        p=(element[1].psrc)
#        print(p)
#        if p == "0c:9f:2d:e4:00:00"
#           then print("Juniper")
print(" ***************IP Node Live*****************\n")
