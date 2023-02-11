import scapy.all as scapy
import time
import subprocess
import netifaces

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def get_default_interface():
    default_gateway = netifaces.gateways()['default'][netifaces.AF_INET][1]
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if default_gateway in netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']:
            return interface
    return None

def sniff(interface):
    while True:
        scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
        time.sleep(600)

def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc
            if real_mac != response_mac:
                print("[+] ARP Spoofing Attack Detected!!")
                print("[+] Blocking Attacker's MAC Address: " + response_mac)
                subprocess.call(["iptables", "-A", "INPUT", "-m", "mac", "--mac-source", response_mac, "-j", "DROP"])
                subprocess.call(["notify-send", "ARP Spoofing Attack Detected!", "Blocking Attacker's MAC Address: " + response_mac])
        except IndexError:
            pass

interface = get_default_interface()
if interface is not None:
    sniff(interface)
else:
    print("[-] Default interface could not be found.")
