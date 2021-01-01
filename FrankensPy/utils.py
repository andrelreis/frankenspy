"""
Miscelaneous of utils functions
"""

from __future__ import absolute_import, division
import numpy as np

def check_region(region):
    '''
    Check the given region values.

    Input
    -----------
    region: tuple - (West,East,South,North)

    Output
    ----------
    ValueError : If regions does not have exactly 4 values, W>=E, or S>=N.

    '''
    if len(region) != 4:
        raise ValueError("Invalid given region'{}'. The list must have 4 values.".format(region))

    w,e,s,n = region
    if w>e:
        raise ValueError("Invalid values'{}'(W,E,S,N). Must have W=<E.".format(region))
    if s>n:
        raise ValueError("Invalid values'{}'(W,E,S,N). Must have S=<N.".format(region))
