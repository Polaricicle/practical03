#Filename: q6_determine_prime.py
#Author: Tan Di Sheng
#Created: 20130218
#Modified: 20130218
#Description: This program shows the first 1000 prime numbers

from math import *

print("This program shows a table of the first 1000 prime numbers.")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def is_prime(n):
        for a in range(2, int(sqrt(n) + 1)):
            if n % a == 0:
                return False
            else:
                return True

    primes = []
    b = 1
    c = 1
    while True:
        b = b + 1
        d = is_prime(b)
        if d == True:
            primes.append(b)
            c = c + 1
            if c > 1000:
                break
            
    e = 0
    while e < 1000:
        print(primes[e], primes[e + 1], primes[e + 2], primes[e + 3], primes[e + 4], primes[e + 5], primes[e + 6], primes[e + 7], primes[e + 8], primes[e + 9])
        e = e + 10
        

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
