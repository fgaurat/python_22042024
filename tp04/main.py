# import fibo as fb
# fb.fib(10)
import sys
from fibo import fib

import mathlib.thefibo
# from mathlib.thefibo import fib

# from fibo import fib as fibi
# from fibo import *

def local_sfib(n):
    print("fib",n)


def main():
    print(sys.argv)
    value = int(sys.argv[-1])
    print(type(value))
    fib(value)

if __name__=='__main__':
    main()

