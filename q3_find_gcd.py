#Filename: q3_find_gcd.py
#Author: Tan Di Sheng
#Created: 20130218
#Modified: 20130218
#Description: This program writes a function that returns the greatest common
#divisor between two positive integers

print("""This program displays a the greatest common divisor between
two positive integers.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def gcd(m, n):
        min = m
        if (min > n):
            min = n

        m = int(m)
        n = int(n)
        min = int(min)

        while not (min == 1):
            if (m % min == 0) and (n % min == 0):
                break
            min = min - 1

        print("\nThe greatest common divisor of {0} and {1} is {2}".format(m, n, min))

    while True:
        m = input("\nEnter the first integer: ")
        n = input("Enter the second integer: ")
        try:
            int(m) and int(n)
        except:
            print("\nPlease input integer values.")
        else:
            break
    gcd(m, n)

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
