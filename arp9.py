import scapy.all as scapy

juniper = "0c:2f:0b"
Extrem  = "0c:6b:b7"
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
print("IP" + " "*20+"MAC"+" "*25+"sender"+ " "*20+"Vendor")
print("***************************************************************************************************")
for element in clients:
	# print(element[1].psrc + "        " + element[1].hwsrc +  "        " + element[1].pdst + "        " + "juniper")
	if element[1].hwsrc.startswith(juniper)== True:
		print(element[1].psrc + "        " + element[1].hwsrc +  "        " + element[1].pdst + "        " + "juniper")

	if element[1].hwsrc.startswith(Extrem)== True:
		 print(element[1].psrc + "        " + element[1].hwsrc +  "        " + element[1].pdst + "        " + "Extrem")

        if element[1].hwsrc.startswith(cisco)== True:
                 print(element[1].psrc + "        " + element[1].hwsrc +  "        " + element[1].pdst + "        " + "cisco")

print(" ****************************************************************************************************")

