side1 =int(input('Enter the first side value'))
side2 =int(input('Enter the second side value'))
side3 =int(input('Enter the Third side value'))

if  side1 == side2 == side3 :
    print('its a equilateral Triangle')
elif (side1== side2 !=side3)or (side2 ==side3 !=side1) or (side1 == side3 !=side2):
    print('its a isosceles Triangle')
else:
    print('its a scalene Triangle')


