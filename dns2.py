#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *


def findDNS(p):
    if p.haslayer(DNS):
        print(p[IP].src, p[DNS].summary())
    sniff(prn=findDNS)
