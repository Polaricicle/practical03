#Filename: q8_convert_milliseconds.py
#Author: Tan Di Sheng
#Created: 20130218
#Modified: 20130218
#Description: This program writes a function that converts milliseconds
#to hours, minutes and seconds.

import random

print("""This program converts a timing in milliseconds to a timing
in hours. minutes and seconds.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def convert_ms(n):
        mas = n % 3600000
        sec = n % 60000
        secs = int(sec / 1000)
        mins = int((mas - sec) / 60000)
        hours = int((n - mas) / 3600000)
        if hours >= 1:
            print("{0}:{1}:{2}".format(hours, mins, secs))
        elif hours == 0 and mins >= 1:
            print("0:{0}:{1}".format(mins, secs))
        elif hours == 0 and mins == 0 and secs >= 1:
            print("0:0:{0}".format(secs))
        


    while True:
        n = input("Enter the integer: ")
        try:
            int(n)
        except:
            print("\nPlease input an integer value.")
        else:
            break

    n = int(n)
    convert_ms(n)

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
