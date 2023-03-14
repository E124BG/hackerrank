#   https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(number):
    # octal
    octal_hundreds = (number // 8*8) * 100
    octal_tens = (number // 8) * 10
    octal_units = number % 8
    octal = octal_tens + octal_units
    print ("octal: ",octal)
    
    #hexadecimal
    hexa_tens = (number // 16) * 10
    hexa_units = number % 16
    hexa = hexa_tens + hexa_units
    print ("hexadecimal: ",hexa)
    
    
    


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)