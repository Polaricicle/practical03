#Filename: q5_compute_series.py
#Author: Tan Di Sheng
#Created: 20130218
#Modified: 20130218
#Description: This program writes a function that computes the sum of a series
#of fractions

print("This program computes the sum of a series of fractions.")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def m(i):
        print ("i m(i)")
        for a in range(1, i + 1, 2):
            positivesums = 0
            negativesums = 0
            sums = 0
            for b in range (1, a + 2, 2):
                positivesums = positivesums + (1 / (2 * b - 1))
                negativesums = negativesums + (1 / (2 * b + 1))
                sums = 4 * (positivesums - negativesums)
            d = a - 1
            print (d, "{0:<10.11f}".format(sums))


    while True:
        i = input("Enter the integer: ")
        try:
            int(i)
        except:
            print("\nPlease input an integer value.")
        else:
            break

    i = int(i)
    m(i)

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
