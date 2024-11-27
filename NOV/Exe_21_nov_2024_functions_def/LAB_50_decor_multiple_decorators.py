def define_ui(func):
    def wrapper():
        print('before url')
        func()
    return wrapper()


def logs_format(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper()

@define_ui
@logs_format
def helo1():
    print('>>>welcome')

helo1()

