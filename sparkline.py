# coding: utf-8
def sparklines(inputitems):
    """
    sparklines(list) -> string
    Returns a string of unicode chars to represent a sparkline graphic
    """

    import string
    
    numlist = [int(x) for x in inputitems]
    maximum = float(max(numlist))
    minimum = float(min(numlist))
    graph = []
    
    for i, num in enumerate(numlist):
        if num/maximum == 1:
            bar = unichr(9608)
            bar.encode('utf-8','ignore')
            graph.append(bar)
        elif num/maximum >= 0.87:
            graph.append(unichr(9607))
        elif num/maximum >= 0.75:
            graph.append(unichr(9606))
        elif num/maximum >= 0.62:
            graph.append(unichr(9605))
        elif num/maximum >= 0.5:
            graph.append(unichr(9604))
        elif num/maximum >= 0.37:
            graph.append(unichr(9603))
        elif num/maximum >= 0.25:
            graph.append(unichr(9602))
        elif num/maximum >= 0.12:
            graph.append(unichr(9601))
        else:
            graph.append(" ")
    
    return u"".join(graph)
