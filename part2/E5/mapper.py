#!/usr/bin/env python
"""mapper.py"""
import json
import sys
import re
from ast import literal_eval


for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words

    sp = re.findall("{.*}", line)

    words = line.replace(sp[0], "").split()

    sp = literal_eval(sp[0])


    print('%s\t%s' % (words[1][0:4],1))
