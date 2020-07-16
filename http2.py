#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *


def findHTTP(p):
    if p.haslayer(TCP):
        if p[TCP].dport == 80:
            if p.haslayer(Raw):
                print(p[Raw].load)

sniff(prn=findHTTP)
