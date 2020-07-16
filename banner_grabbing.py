#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
s = socket.socket()

s.connect(("ad.samsclass.info", 22))
print(s.recv(2014).decode())
s.close()