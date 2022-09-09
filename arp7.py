import scapy.all as scapy

juniper = "0c:a1:4b"

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
	if element['mac'].startswith(juniper):
	   print(element[1].psrc + "        " + element[1].hwsrc +  "        " + element[1].pdst + "        " + "juniper")

print(" ***************IP Node Live*****************\n")

