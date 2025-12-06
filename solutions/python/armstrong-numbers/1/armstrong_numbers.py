import math
def is_armstrong_number(number):
    somme = 0
    n= number
    long = len(str(number))
    while n >= 1:
        u = n % 10
        somme += u**long
        n //= 10
    print(somme, number)
    
    return somme == number


