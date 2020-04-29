#!/bin/python3

import sys
import math

# arg 1 = pourcentage par mois
# arg 2 = ajout par mois
# arg 3 = duree en mois
# arg 4 = starting value

try:
    percent = float(sys.argv[1])
except IndexError:
    percent = 0.2
except ValueError:
    print("python3 main.py <percentage> <monthly_added_value> <month_number> <value_starting_with>")
    exit()

try:
    addon = float(sys.argv[2])
    month  = float(sys.argv[3])
    starting = float(sys.argv[4])
except IndexError:
    addon, month, starting = 100.0, 120.0, 1000.0

value = starting
for i in range(0, int(month)):
    percent_to_add = value * (percent / 100)
    value += math.floor(percent_to_add)
    value += addon
    if i != 0 and i % 12 == 0: 
        print(f"Year {i / 12}, value = {value}")

print(f"Month {int(month)} = {'%.2f'%(value)} with an increase of {'%.2f'%(percent)}% and {'%.2f'%(addon)}$ per month, for {int(month)} months, starting with {'%.2f'%(starting)}$")

