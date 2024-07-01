#!usr/bin/env python3

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = input("Enter hours: ")
rate  = input("Enter rate per hour: ")
d = float(rate) * int(hours)
c = 24 * 7
if d == c:
    print("Your weekly earning is ",d)
else:
    print("Your weekly earning is ",d)

