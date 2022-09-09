def scan_ips(interface='ens3', ips='192.168.174.0/24'):
	"""a simple ARP scan with Scapy"""
	try:
		print('[*] Start to scan')
		conf.verb = 0 # hide all verbose of scapy
		ether = Ether(dst="ff:ff:ff:ff:ff:ff")
		arp = ARP(pdst = ips)
		answer, unanswered = srp(ether/arp, timeout = 2, iface = interface, inter = 0.1)

		for sent, received in answer:
			print(received.summary())

	except KeyboardInterrupt:
		print('[*] User requested Shutdown')
		print('[*] Quitting...')
		sys.exit(1) 
