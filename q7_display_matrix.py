#Filename: q7_display_matrix.py
#Author: Tan Di Sheng
#Created: 20130218
#Modified: 20130218
#Description: This program writes a function that displays an n by n matrix
#where n is a positive integer entered by the user.

import random

print("This program computes the sum of a series of fractions.")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def print_matrix(n):
        elements = []
        for i in range (1, n * n):
            a = random.randint(0, 1)
            elements.append(a)
        for h in range (0, n):
            for j in range (0, n):
                b = random.randint(0, 1)
                print (b, end=" ")
            print ("")
        


    while True:
        n = input("Enter the integer: ")
        try:
            int(n)
        except:
            print("\nPlease input an integer value.")
        else:
            break

    n = int(n)
    print_matrix(n)

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
