# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 15:57:33 2020

@author: nataa

Towers of hanoi: A Complete Recursive Visualization
https://www.youtube.com/watch?v=rf6uf3jNjbo&feature=youtu.be
"""
def hanoi(n, start, end):
    """    
    Prints the list of steps required to move n disks from the start to move n 
    disks from the start rod to the end rod
    >>> hanoi(2,1,3)
    1->3
    1->3
    2->3
    """
    if n == 1:
        pm(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n-1, start, other)
        pm(start, end)
        hanoi(n-1, other, end)
    
def  pm(start, end):
    """
    Prints a move in the correct format
    >>> pm(1,3)
    1 - 3
    """
    print(start,'->', end)
    

hanoi(2,1,3)