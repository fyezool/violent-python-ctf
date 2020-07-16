#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket()
s.connect(("ad.samsclass.info", 10102))
print(s.recv(1024).decode())
s.send("Goodbye\n".encode())
print(s.recv(1024).decode())
s.close()
