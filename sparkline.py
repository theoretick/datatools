#!/usr/bin/env python
# -*- coding: UTF-8 -*-
def sparkline(inputitems):
    """
    sparkline(list) -> string
    Returns a string of unicode chars to represent a sparkline graphic

    v2 - uses unicode chars from string instead of function calls
    """
    import string
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    numlist = [int(x) for x in inputitems]
    maximum = float(max(numlist))
    minimum = float(min(numlist))
    graph = []
    bars = u"▁▂▃▄▅▆▇█"
    pos = len(bars)
    
    for i, num in enumerate(numlist):
        if num/maximum == 1:
            graph.append(bars[pos-1])
        elif num/maximum >= 0.87:
            graph.append(bars[pos-2])
        elif num/maximum >= 0.75:
            graph.append(bars[pos-3])
        elif num/maximum >= 0.62:
            graph.append(bars[pos-4])
        elif num/maximum >= 0.5:
            graph.append(bars[pos-6])
        elif num/maximum >= 0.25:
            graph.append(bars[pos-7])
        elif num/maximum >= 0.12:
            graph.append(bars[pos-8])
        else:
            graph.append(" ")
            print "appended blank"

    graphstr = "".join(graph)

    print graphstr," is type: ",type(graphstr)
    print "".join(graph)   
    return graphstr.encode('utf-8')
