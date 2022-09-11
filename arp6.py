#!/usr/bin/env python

# Suppress Scapy IPv6 warning
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Begin our Scapy script.
from scapy.all import *



#from scapy.all import ARP, Ether, srp
import socket
# importing main functions from Scapy and Socket

mac_key = '0c:a1:4b:2e:00:00'
# Target value for first three fields of MAC address

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
#target_ip = ("192.168.{}.0/24".format(IPAddr[6]))
target_ip = ("192.168.174.0/24".format(IPAddr[6]))
# Assigning index value for third section of IP address
# To make third section of target_ip a variable determined by host
# "/24" denotes IP address spectrum for the ARP packet destination

arp = ARP (pdst=target_ip)
# Creating ARP packet assigned to "target_ip"

ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# Creating Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting

packet = ether/arp
# Stacking

result = srp(packet, timeout=5, verbose=3)[0]
# Defining result with timeout parameter

clients= []
# Client list to be finished below

for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    # For each response, append ip and mac address to 'clients' list

print("Devices On This Network:")
print("IP" + " "*30+"MAC")
# Print table of accumulated data

for client in clients:
    print("{:3}    {}".format(client['ip'], client['mac'].startswith(mac_key)))
# Printing IP addresses and assosciated MACs from clients list
# With bool checking against mac_key
