#!/usr/bin/python3

import sys

p = sys.platform
print("Type=", type(p))
print("Platform = ", p)

v = sys.version
print("version =", v)

pa = sys.path
print("\npath = ", pa)

arg = sys.argv
print("\n type arg = ", arg)

print(arg[0])
print(arg[1])
print(arg[2])
