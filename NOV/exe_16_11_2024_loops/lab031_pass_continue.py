for i in range(1,20):
    if i % 2 == 0:
        pass # the execution will print the next line
        print(i)

for i in range(1,20):
    if i % 2 == 0:
        continue # loop will traverse back to the main statement
        print(i)