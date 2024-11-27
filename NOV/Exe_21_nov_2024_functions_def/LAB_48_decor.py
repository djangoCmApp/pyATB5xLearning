def define_ui(func):

    def url_wrapper():
        print('before url')
        print('url is needed')
        func()
        print('after url')
        print('url tested')
    return url_wrapper()



@define_ui
def login():
    print('>>this is login function')
    print('>>login successfull')

@define_ui
def main_page():
    print('>>this is login function')
    print('>>main page loaded successfully')

