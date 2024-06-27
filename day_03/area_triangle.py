#!/usr/bin/env python3

"""
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
        Enter height: 10
            The area of the triangle is 100
"""

b = input("Enter base: ")
h = input("Enter height: ")
area = int(0.5 * int(b) * float(h))
print("The area of the triangle is ",area)


