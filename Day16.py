#!/bin/python3

import sys
#S = input().strip()
try:
    print(int(input().strip()))
except ValueError:
    print("Bad String")
