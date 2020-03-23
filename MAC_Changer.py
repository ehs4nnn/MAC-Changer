#!/usr/bin/evm python

import subprocess
import optparse
import re

def mac_cahnger(interface, new_mac):
	print("[+] Changeing MAC Address For " + interface + " To " + new_mac)
	subprocess.call(["sudo", "ifconfig", interface, "down"])
	subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["sudo", "ifconfig", interface, "up"])



def parser_help():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Using This Options To Put Your Interface")
	parser.add_option("-m", "--mac", dest="new_mac", help="Using This Options To Put A MAC Address")
	(options, arguments) = parser.parse_args()
	if not options.interface: #we say if interface not puted by user show a msg
		parser.error("[-] Please Put Your Interface, And Using The --help For More Info")
	elif not options.new_mac: #we say if mac address not puted by user show a msg
		parser.error("[-] Please Put A New MAC Address, And Using --help For More Info")
	return options #we return the option for line 28

def get_current_mac(interface):
	ifconf_result = subprocess.check_output(["ifconfig", interface])
	mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconf_result)
	if mac_address_result:
		return mac_address_result.group(0)
	else:
		print("[-] could not find the MAC Address")



options = parser_help()
currentm = get_current_mac(options.interface)
print("Current Mac = " + str(currentm))
mac_cahnger(options.interface, options.new_mac)

if currentm == options.new_mac:
	print("[+] MAC address was successfully changed to " + currentm)
else:
	print("[-] MAC address did not get the change")
