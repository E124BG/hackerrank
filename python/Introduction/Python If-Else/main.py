# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("please input the number: "))
    
    if n % 2 == 1:
        print("Weird")
    elif (2 <= n) and (n <= 5):
        print("Not Weird")
    elif (6 <= n) and (n <= 20):
        print("Weird")
    elif n > 20:
        print("Not Weird")