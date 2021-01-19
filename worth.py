#!/bin/python3

import sys
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--percent", help="Monthly percentage to add.", default=0.2, type=float)
parser.add_argument("-a", "--addon", help="Monthly amout you add.", default=100.0, type=float)
parser.add_argument("-m", "--month", help="Duration in month", default=120.0, type=float)
parser.add_argument("-s", "--starting", help="Starting value", default=1000.0, type=float)
args = parser.parse_args()

print(args)

value = args.starting
for i in range(0, int(args.month)):
    percent_to_add = value * (args.percent / 100)
    value += math.floor(percent_to_add)
    value += args.addon
    if i != 0 and i % 12 == 0: 
        print(f"Year {i / 12}, value = {value}")

print(f"""
        Month {int(args.month)} = {'%.2f'%(value)} with an increase of 
        {'%.2f'%(args.percent)}% and {'%.2f'%(args.addon)}$ per month, for 
        {int(args.month)} months, starting with {'%.2f'%(args.starting)}$
    """)