Some assorted python data tools I've been working on.

##Sparkline##

Generates sparklines from list parameter:

    >>> sparkline([1,1,2,2,3,3,4,4,2,2,3,4])
    ▂▂▃▃▆▆██▃▃▆█
    >>> sparkline([122,14,3,3,4,30,50,90])
    █    ▁▂▅

###Todo###

Currently deciding on how to properly deal with scale, as can be seen from above.