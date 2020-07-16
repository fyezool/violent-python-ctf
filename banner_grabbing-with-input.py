#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket()
s.settimeout(2)

port = int(input("port number:"))

s.connect(("target1.bowneconsulting.com", port))
print(s.recv(2048).decode())
s.close
