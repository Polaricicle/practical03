#Filename: q1_display_reverse.py
#Author: Tan Di Sheng
#Created: 20130218
#Modified: 20130218
#Description: This program displays an integer in reverse order

print("This program displays an integer in reverse order.")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def reverse_int(n):
        print(n[::-1])

    while True:
        n = input("\nEnter an integer: ")
        try:
            int(n)
        except:
            print("\nPlease input an integer")
        else:
             break
        
    reverse_int(n)

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
