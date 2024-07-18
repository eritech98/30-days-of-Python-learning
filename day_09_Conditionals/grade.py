#!usr/bin/env python3

'''
Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

'''

def grade():
    user = int(input("Enter your grade: "))
    if user >= 80 and user <= 100:
        print("Your score is A")
    elif user >= 70 and user <= 89:
        print("Your score is B")
    elif user >= 60 and user <= 69:
        print("Your score is C")
    elif user >= 50 and user <= 59:
        print("Your score is D")
    elif user >= 0 and user <= 49:
        print("Your Score is F")
    else:
        print("Invalid score")
grade()
