#!usr/bin/env python3

#Use and operator to check if 'on' is found in both 'python' and 'dragon'

def and_operator():
    a = str("python")
    b = str("dragon")
    if "on" in a and b:
        print("'on' is in both 'dragon' and 'python'")
    else:
        print("on is not found in both 'dragon' and 'python'")
and_operator()


