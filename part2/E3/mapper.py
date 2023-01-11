#!/usr/bin/env python
"""mapper.py"""
import json
import sys
import re
from ast import literal_eval

p = 1
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words

    sp = re.findall("{.*}", line)

    words = line.replace(sp[0], "").split()

    sp = literal_eval(sp[0])

    print('%s\t%s' % (1,len(words[0])))

    p +=1

print('%s\t%s' % (2,p))

