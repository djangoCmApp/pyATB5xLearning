global_var_b =12 #global variable

def my_function():
    global_var_a =20 #local variable
    print(global_var_b)
    print(global_var_a)

 #print(global_var_a) # not allowed
print(global_var_b)# allowed
my_function()