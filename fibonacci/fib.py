import sys


def fib(curr, next):
    print curr
    curr = next
    next += curr
    if curr < 200: 
        fib(curr, next)

fib(1, 1)
