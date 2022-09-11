def callback(self, packet):
        flags = packet.sprintf("%TCP.flags%")
        proto = IP
        if IPv6 in packet:
            proto = IPv6
        if flags == "A" and not self.ignore_packet(packet, proto):
            src_mac = packet[Ether].src
            dst_mac = packet[Ether].dst
            src_ip = packet[proto].src
            dst_ip = packet[proto].dst
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            seq = packet[TCP].seq
            ack = packet[TCP].ack
            if self.verbose:
                print("RST from %s:%s (%s) --> %s:%s (%s) w/ %s" % (src_ip, src_port, src_mac, dst_ip, dst_port, dst_mac, ack))
            if self.noisy:
                self.send(self.build_packet(src_mac, dst_mac, src_ip, dst_ip, src_port, dst_port, seq, proto))
            self.send(self.build_packet(dst_mac, src_mac, dst_ip, src_ip, dst_port, src_port, ack, proto))
