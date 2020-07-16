#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

r = requests.get("https://samsclass.info")
print(r.status_code)
