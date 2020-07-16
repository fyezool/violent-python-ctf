#!/usr/bin/env python
# -*- coding: utf-8 -*-

greet = "Hello, World!"
print(greet)

print("Start: ", greet[0:3])
print("Middle: ", greet[3:6])
print("End: ", greet[-3:])

a = greet.find(",")

print("Portion before comma", greet[:a])
