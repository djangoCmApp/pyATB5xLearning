# Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.

year =int(input('enter the year'))

if year % 4 ==0 and year % 400 !=100 :
    print('its a leap year')
elif year % 100 != 0:
    print('its not a leap year')
else :
    print('enter valid year')


