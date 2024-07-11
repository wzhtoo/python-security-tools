import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()


scan("192.168.1.1/24")
