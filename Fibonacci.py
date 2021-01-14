# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:47:29 2020

@author: nataa

Recursion, the Fibonacci Sequence and Memoization
https://www.youtube.com/watch?v=Qk0zUZW-U_M
"""

from functools import lru_cache

@lru_cache(maxsize = 1000) #By 
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    
# for n in range(1,20):
#    print(n," : ", fibonacci(n))
# Muere al llegar al fibonacci 30, es decir se vuelve muuy lenta


"""
    Memoization. 
    Guarda valores obtenidos anteriormente y los reutiliza para ahorrar tiempo
    y realizar menos operaciones
    1. Implement explicitly

fibonacci_cache = {}
def fibonacci(n):
    # If we have cached the value, the return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
        
    # Cache the value and return it
    fibonacci_cache[n] = value
    return value
"""

for n in range(1, 100):
    print(n," : ", fibonacci(n))