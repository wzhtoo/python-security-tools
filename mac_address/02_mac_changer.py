import subprocess

interface = "wlan0"
new_mac = "00:11:22:33:44:77"

print("[+] Changing Mac address for ", interface + " to " + new_mac)


# subprocess.call("ifconfig wlan0 down", shell=True)
# subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66", shell=True)
# subprocess.call("ifconfig wlan0 up", shell=True)

