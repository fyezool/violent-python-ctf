#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

h = hashlib.new('md4', 'password'.encode("utf-16le"))
print(h.hexdigest)
