#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

username = 'admin'

for num in range(10,100):
    message = 'admin'+ ':' + 'password' + str(num)
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print(base64_message)
