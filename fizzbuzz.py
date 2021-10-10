#!/usr/env python3

"""
Write a program to print numbers from 1 to 100.
But for multiples of 3 print 'Fizz' instead and
    for the multiple of 5 print 'Buzz' and
    for the numbers multiple of both 3 and 5 print 'FizzBuzz'.
"""

import sys
import time


def fizz_buzz1(r_min, r_max):
    """
    Straight solution
    """
    result = []
    for num in range(r_min, r_max + 1):
        if num % 15 == 0:
            result.append('FuzzFuzz')
        elif num % 3 == 0:
            result.append('Fizz')
        elif num % 5 == 0:
            result.append('Buzz')
        else:
            result.append(num)
    return result


def fizz_buzz2(r_min, r_max):
    """
    With ternary condition
    """
    return list(
        ('' if num % 3 else 'Fizz') +
        ('' if num % 5 else 'Buzz') or
        num for num in range(r_min, r_max + 1)
    )


def fizz_buzz3(r_min, r_max):
    """
    With ternary condition, map and lambda
    """
    return list(
        map(
            lambda num:
                ('Fizz' if num % 3 == 0 else '') +
                ('Buzz' if num % 5 == 0 else '') or
                num, range(r_min, r_max + 1)
        )
    )


def main(r_min=1, r_max=101):
    """
    Execute all fizz_buzz functions, print and measure results
    """
    fizz_buzz_all = (
        fizz_buzz1(r_min, r_max),
        fizz_buzz2(r_min, r_max),
        fizz_buzz3(r_min, r_max)
    )
    for f in fizz_buzz_all:
        start = time.time()
        print(*f, sep='\n')
        end = time.time()
        print("Execution time: ", end - start)


if __name__ == "__main__":
    sys.exit(main())
