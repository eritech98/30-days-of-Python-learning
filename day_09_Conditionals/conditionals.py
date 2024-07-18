#!usr/bin/env python3

'''
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive

'''

def Erick():
    user = int(input("Enter your age: "))
    if user >= 18:
        print("You are old enough to drive")
    elif int(user) < 18:
        print('You need {} more years to learn to drive\n\n'.format(20 - int(user)))

    '''
    Compare the values of my_age and your_age using if … else. 
    
    Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
    
    You can use a nested condition to print 'year' for 1 year difference in age, 
    
    'years' for bigger differences, and a custom text if my_age = your_age. Output:
    
    Enter your age: 30 You are 5 years older than me.
    
    '''

    your_age,my_age = int(input("Enter your age: ")),26
    if my_age > your_age:
        print('You are {} younger than me'.format(my_age - your_age))
    elif your_age > my_age:
        print('You are {} older than me'.format(your_age - my_age))
    else:
        print("We are same age")




Erick()
