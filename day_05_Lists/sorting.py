#!/usr/bin/env python3

'''
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
'''
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

sorting = ages.sort()

print("\n",ages,"\n",'The minimum age is {} while the maximum age is {}'.format(ages[0],ages[9]))

#Add the min age and the max age again to the list

adding1 = ages.append(19)
adding2 = ages.append(26)

print(ages)

#Find the median age (one middle item or two middle items divided by two)

print(len(ages))

sorting2 = ages.sort()
print(ages)

add = (ages[5] + ages[6])/2

print('The median of the above List is {}'.format(add))

#Find the average age (sum of all items divided by their number )
average = sum(ages)/12
print('The average of the ages in the list is {}'.format(average))

#Find the range of the ages (max minus min)
rang = (max(ages) - min(ages))
print('The range of the ages is Maximum age minus minimum age which is {}'.format(rang))

'''
Compare the value of (min - average) and (max - average), use abs() method
'''
minA = min(ages) - average
maxA = max(ages) - average

Compare = abs(minA)
Compare1 = abs(maxA)

print('After comparison,we get {} for the minimum age and {} for the Maximum age value'.format(Compare,Compare1))
