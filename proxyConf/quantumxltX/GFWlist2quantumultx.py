#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from urllib.request import urlopen
import base64
import re

prefix="DOMAIN-SUFFIX,"
suffix=",Proxy\n"

final_direct=["\n", "FINAL,DIRECT", "\n", "\n"]

def write2conf():
    FROM = "./gfwlist.txt"
    CUSTOMIZED = "./customized_rules.txt"
    TO = "./quantumultX.list"

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