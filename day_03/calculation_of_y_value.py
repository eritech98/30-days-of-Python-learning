#!/usr/bin/env python3

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = input("Enter x: ")
a = (float(x) * float(x))
b = 6 * float(x) + 9

y = a + b

if y == 0:
    print("y equals to zero")
elif y != 0:
    print("Y is not equal to zero")
else:
    print("Try again another number")
print()
print("The value of y is ",y,"and the value of x","is",x)

print()
if  y > 0:
    print("Try a lower number")
elif y < 0:
    print("Try a higher number")

print("From my program,I found out the answer is -3.0")

