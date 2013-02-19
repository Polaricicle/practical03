#Filename: q4_sum_series.py
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
        for a in range(2, i + 1):
            sums = 0
            for b in range (2, a + 1):
                sums = sums + ((b - 1) / b)
            c = a - 1
            print (c, "{0:<10.4f}".format(sums))


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
