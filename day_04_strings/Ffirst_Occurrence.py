#!usr/bin/env python3

'''

Use index to determine the position of 

the first occurrence of F in Coding For All

'''


def Olando():
    string = "Coding For All"
    finding = string.rfind("F")
    if "F" in string:
        print("The index of 'F' is",finding)
    else:
        print("Invalid")
Olando()
