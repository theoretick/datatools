#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#---------------------------------------
# name: sparkline.py
# author: lucas c
# url: github.com/theoretick
#
# inspired by https://github.com/holman/spark
#---------------------------------------

def sparkline(inputitems):
    """
    sparkline(list) -> string
    Returns a string of unicode chars to represent a sparkline graphic
    """

    # invalid input check
    if not isinstance(inputitems, list):
        raise TypeError,"invalid input, must be list"
    
    numlist = [float(x) for x in inputitems]
    maximum = max(numlist)
    minimum = min(numlist)
    total = maximum-minimum
    if total == 0:
        total = 1

    graph = []
    bars = u"▁▂▃▄▅▆▇█"
    
    for i, num in enumerate(numlist):
        pos = num - minimum
        if pos/total == 1:
            graph.append(bars[7])
        elif pos/total >= 0.87:
            graph.append(bars[6])
        elif pos/total >= 0.75:
            graph.append(bars[5])
        elif pos/total >= 0.62:
            graph.append(bars[4])
        elif pos/total >= 0.5:
            graph.append(bars[3])
        elif pos/total >= 0.25:
            graph.append(bars[2])
        elif pos/total >= 0.12:
            graph.append(bars[1])
        else:
            graph.append(bars[0])

    print "".join(graph)

if __name__=='__main__':
    import sys
    args = sys.argv[1].split(",")
    sparkline(args)
