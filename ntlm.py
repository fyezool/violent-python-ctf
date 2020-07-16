#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii
import hashlib

for a in range(00,100):
    hash = hashlib.new('md4', str(a).encode('utf-16le')).digest()
    print(binascii.hexlify(hash))
