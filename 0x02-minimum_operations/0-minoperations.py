#!/usr/bin/python3

"""
minioperations
"""


def minOperations(n):
    '''minioperations'''
    no = 0
    mo = 2
    while n > 1:
        while n % mo == 0:
            no += mo
            n /= mo
        mo += 1
    return no
