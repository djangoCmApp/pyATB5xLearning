# Match statement is like switch  in java
#python >3.10
import match

#syntax
# match variable
    #case pattern:
        #block
#program to build and select a browser name
browser_name =input('Enter the browser Name \n')

match browser_name:
    case "firefox":
        print("starting firefox browser")
    case "Chrome":
        print("starting chrome browser")
    case "Internet explorer":
        print("starting Internet explorer browser")
    case _:
        print('no browser selected')

