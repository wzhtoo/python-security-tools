import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    # print(answered_list.summary())
    # print(answered, unanswered)
    for element in answered_list:
        print("ip source: ", element[1].psrc)
        print("hardware source ", element[1].hwsrc)
        print("------------------------------")


scan("192.168.1.1/24")
