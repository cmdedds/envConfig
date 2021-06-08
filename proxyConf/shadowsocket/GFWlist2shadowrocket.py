#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from urllib.request import urlopen
import base64
import re

prefix="DOMAIN-SUFFIX,"
suffix=",Proxy\n"
conf_start='''# proxy rules for shadowrocket
# by Alan Lee

[General]
bypass-system = true
skip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, localhost, *.local, e.crashlytics.com, captive.apple.com
bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,224.0.0.0/4,255.255.255.255/32
dns-server = system, 114.114.114.114, 112.124.47.27, 8.8.8.8, 8.8.4.4

[Rule]

IP-CIDR,192.168.0.0/16,DIRECT
IP-CIDR,10.0.0.0/8,DIRECT
IP-CIDR,172.16.0.0/12,DIRECT
IP-CIDR,127.0.0.0/8,DIRECT

'''

final_direct=["\n", "FINAL,DIRECT", "\n", "\n"]

def write2conf():
    FROM = "./gfwlist.txt"
    CUSTOMIZED = "./customized_rules.txt"
    TO = "./proxylist.conf"

    total_proxy = []

    with open(FROM, "r") as file:
        for line in file:
            if line.startswith('||'):
                total_proxy.append(prefix + line[2:].rstrip() + suffix)
            elif line.startswith('.'):
                total_proxy.append(prefix + line[1:].rstrip() + suffix)

    with open(CUSTOMIZED, "r") as file:
        for line in file:
            total_proxy.append(line)

    total_proxy = list(set(total_proxy))
    total_proxy.sort()

    with open(TO, "w") as file:
        file.write(conf_start)
        file.writelines(total_proxy)
        file.writelines(final_direct)

def getGFW():
    with urlopen("https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt") as gfwUrl:
        return gfwUrl.read()

def decodeGFW(altchars=b'+/'):
    data = getGFW()
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    gfw = base64.b64decode(data, altchars)
    
    with open("./gfwlist.txt", 'w') as file:
        file.writelines(gfw.decode('utf-8'))

def main():
    decodeGFW()
    write2conf()

main()