#!/usr/bin/python
# -*- coding: UTF-8 -*-
def sparkline(inputitems):
    """
    sparkline(list) -> string
    Returns a string of unicode chars to represent a sparkline graphic
    """
    
    numlist = [int(x) for x in inputitems]
    maximum = float(max(numlist))
    minimum = float(min(numlist))
    graph = []
    bars = u"▁▂▃▄▅▆▇█"
    
    for i, num in enumerate(numlist):
        if num/maximum == 1:
            graph.append(bars[7])
        elif num/maximum >= 0.87:
            graph.append(bars[6])
        elif num/maximum >= 0.75:
            graph.append(bars[5])
        elif num/maximum >= 0.62:
            graph.append(bars[4])
        elif num/maximum >= 0.5:
            graph.append(bars[3])
        elif num/maximum >= 0.25:
            graph.append(bars[2])
        elif num/maximum >= 0.12:
            graph.append(bars[1])
        else:
            graph.append(bars[0])

    graphstr = "".join(graph)
    print graphstr
