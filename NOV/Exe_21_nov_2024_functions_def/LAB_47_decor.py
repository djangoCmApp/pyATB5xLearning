def define_security(func):

    def wrapper():
        print('before driving')
        print('licence,helmet,jacket')
        func()
        print('take the keys')
        print('park the vehical in a safe place')
    return wrapper()



@define_ui
def scooty():
    print('>>the acutual function')
    print('>>i can ride a scooty')

@define_security
def ola_scooty():
    print('>>i can ride a OLA scooty')
