number1 =int(input('enter first no'))
number2 =float(input('enter second no'))
number3 = int(input('enter third no'))

if number1 >number2 and number1 > number3:
    print(number1,'is the maximum number')

elif number2 >number1 and number2 > number3:
    print(number2, 'is the maximum number',)
else:
    print(number3,'is max')
