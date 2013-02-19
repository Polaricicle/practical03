#Filename: q2_display_pattern.py
#Author: Tan Di Sheng
#Created: 20130218
#Modified: 20130218
#Description: This program displays a pattern

print("This program displays a pattern.")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def display_pattern(n):
        last = 0
        for i in range (1, n + 1):
            last = str(last) + str(i) + " "
        for i in range (1, n + 1):
            if i < 10:
                spaces = i * 2
            elif 10 <= i < 100:
                spaces = 18 + 3 * (i - 9)
            elif 100 <= i < 1000:
                spaces = 198 + 4 * (i - 9)
            elif 1000 <= i < 10000:
                spaces = 468 + 5 * (i - 9)
            print(" " * (len(last) - spaces), end = "")
            for a in range(i, 0, -1):
                print (a, end=" ")
            print ()
            
    while True:
        n = input("\nEnter an integer: ")
        try:
            int(n)
        except:
            print("\nPlease input an integer")
        else:
             break
            
    n = int(n)
    display_pattern(n)

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
