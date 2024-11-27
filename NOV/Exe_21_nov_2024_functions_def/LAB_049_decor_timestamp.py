import time

def define_ui(func):

    def time_wrapper():
        start_time = time.time()
        print('starttime',start_time)
        func()
        end_time = time.time()
        print('endtime', end_time)
        print('totaltime',end_time - start_time)
    return time_wrapper()




@define_ui
def login():
    print('>>this is login function')
    print('>>login successfull')
    time.sleep(2)


@define_ui
def main_page():
    print('>>this is login function')
    print('>>main page loaded successfully')
    time.sleep(6)