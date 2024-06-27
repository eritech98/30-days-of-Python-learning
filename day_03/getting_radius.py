#!/usr/bin/env python3

"""
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

"""

r = input("Put radius of a circle: ")
pi = float(3.14)
area = pi * int(r)**2
circumference = 2 * pi * int(r) 
print("The radius of the cicle is", r,"\n","The area of the cicle is: ", area,"\n","The circumference of the cicle is: ",circumference)



