#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_key = None
current_value1 = 0
current_value2 = 0
key = None

list = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value1, value2 = line.split('\t')

    # convert value (currently a string) to int
    try:
        value1 = int(value1)
        value2 = int(value2)
    except ValueError:
        # value was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: key) before it is passed to the reducer
    if current_key == key:
        current_value1 += value1
        current_value2 += 1
    else:
        if current_key:
            # write result to STDOUT
            list.append([current_key, current_value1, current_value2])
            # print('%s\t%s' % (current_key, current_value))
        current_value1 = value1
        current_value2 = value2
        current_key = key

# do not forget to output the last key if needed!
if current_key == key:
    list.append([current_key, current_value1, current_value2])
    # print('%s\t%s' % (current_key, current_value))

for item in sorted(list,key=lambda x: x[0],reverse=True):
    print('%s\t%s' % (item[0], float(item[1])/float(item[2])))