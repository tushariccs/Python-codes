# a = 10  # global variable


# def localScope():
#     a = 15
#     print("Inside (Local Scope)", a)


# localScope()
# print("Outside(Global Variable)", a)

# b = 15  # global variable


# def localScope():
#     # but after writing global b then above variable is used
#     global b
#     b = 15  # currently it is global
#     # here we don't have a local variable
#     # here the point is that we can't create local variable with same name
#     # so we use the method called as globals
#     print("Inside (Global Variable)", b)


# localScope()
# print("Outside(Global Variable)", b)


a = 15
print(id(a))


def localGlobalScope():
    a = 10
    # Here we want to acess the global variable then we can use globals()
    x = globals()['a']
    # here it will take all globals variable
    # For eg there can be many global variables in above scope
    # To access the specific one we need [variable_name]
    print(id(x))
    # We can observe that they are pointing to same memory location.
    print("Global variable a is acessed i.e a here: ", x)


localGlobalScope()
print(a)
