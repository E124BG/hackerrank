# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    
    print(leap)
    return leap

year = int(input())

is_leap(year)