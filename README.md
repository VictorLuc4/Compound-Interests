# Compound interests

This programs calculate the compounds interest dependig on the params you add.

## Usage
How to use it : 
``` bash
usage: worth.py [-h] [-p PERCENT] [-a ADDON] [-m MONTH] [-s STARTING]

optional arguments:
  -h, --help                        show this help message and exit
  -p PERCENT, --percent PERCENT     Monthly percentage to add.
  -a ADDON, --addon ADDON           Monthly amout you add.
  -m MONTH, --month MONTH           Duration in month
  -s STARTING, --starting STARTING  Starting value
```

## Output example

```text
Year 1.0, value = 2337.0
Year 2.0, value = 3600.0
Year 3.0, value = 4895.0
Year 4.0, value = 6221.0
Year 5.0, value = 7579.0
Year 6.0, value = 8971.0
Year 7.0, value = 10396.0
Year 8.0, value = 11856.0
Year 9.0, value = 13350.0

        Month 120 = 14751.00 with an increase of 
        0.20% and 100.00$ per month, for 
        120 months, starting with 1000.00$
```