import subprocess

# interface = "wlan0"
# python_2
# interface = raw_input(" interface > ")
# interface = raw_input(" new Mac > ")

# python3
interface = input(' interface > ')
new_mac = input(" new MAC > ")

print("[+] Changing Mac address for ", interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

