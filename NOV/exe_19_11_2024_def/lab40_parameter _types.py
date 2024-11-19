#no return type and parameter
from nltk.tag.brill import nltkdemo18


def hello():
    print('hi')
#no return with parameter
def sayhi(name):
    print('hi',name)
#no return type with default arguments
def sayhi2(name ='kavya'):
    print('hi',name)
#no return and multiple parameters
def multi(firstname ='kavya',lastname='srinivas'):
    print(firstname,lastname)

multi()
multi(firstname ='nishanth')
multi(lastname ='bn')
multi(firstname ='nishanth',lastname= 'bn')


#with parameter and return type

n1 =int(input('enter first number'))
n2 =int(input('enter second number'))
n3 =int(input('enter third number'))

def add(num1=100,num2=200,num3 =300):
    return num1+num2+num3
#defined parameter
result = add(n1,n2,n3)
print(result)

#default parameter
result2 =add()
print(result2)



