def details(name):
    print("hello",name)
    print(f"hello {name}")

details('world')

def check():
    print('calling details function')
    details('world in side check')

check()