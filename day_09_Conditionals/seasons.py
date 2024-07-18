#!usr/bin/env python3

'''
Check if the season is Autumn, Winter, Spring or Summer.

If the user input is: September, October or November, the season is Autumn.

December, January or February, the season is Winter.

March, April or May, the season is Spring June, July or August, the season is Summer

'''
def season():
    things = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    user = str(input("Please input any months here: "))
    if things[0] == user:
        print("The season is Winter")

    elif things[1]  == user:
        print("The season is Winter")

    elif things[11] == user:
        print("The season is winter")

    elif things[8] == user:
        print("The season is Autumn")

    elif things[9] == user:
        print("The season is Autumn")

    elif things[10] == user:
        print("The season is Autumn")

    elif things[2] == user:
        print("The season is Spring")

    elif things[3] == user:
        print("The season is Spring")

    elif things[4] == user:
        print("The season is Spring")

    elif things[5] == user:
        print("The season is summer")

    elif things[6] == user:
        print("The season is Summer")

    elif things[7] == user:
        print("The season is Summer")

    else:
        print("Invalid!")
season()

