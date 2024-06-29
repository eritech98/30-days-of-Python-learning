#!/usr/bin/env python3

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

def Euclidean():
    x1 = 2
    y1 = 2
    x2 = 6
    y2 = 10
    m = ((int(y2) - int(y1))/(int(x2) - int(x1)))
    
    dist = int(x2) - int(x1)
    dist1 = int(y2) - int(y1)

    print("The slope m is ",m,"and the Euclidean distance between point (2, 2) and point (6,10) is","(",dist,",",dist1,")")
    
Euclidean()



