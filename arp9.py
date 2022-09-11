import scapy.all as scapy

juniper = "00:50:56"
Extrem  = "0c:a1:4b"
cisco   = "9a:f2:07"


request = scapy.ARP()
x = raw_input("Enter IP address: ")
request.pdst = x

broadcast = scapy.Ether()
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout = 1)[0]

print("***************************************************************************************************")
print("IP" + " "*20+"MAC"+" "*20+"sender"+ " "*20+"Vendor")
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

