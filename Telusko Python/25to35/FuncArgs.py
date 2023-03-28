
# def person(name, age):
#     print(name)
#     print(age)


# person(name=28, age="Tushar")

# # default parameter


# def add(a, b=18):
#     c = a + b
#     return c


# c = add(5)
# print(c)

# varying length argument
# def add(*b):
#     c = 0
#     for i in b:
#         c = c + i
#     return c


# c = add(5, 6, 7, 8)
# print(c)
# # if __name__ == "__main__":
# #     person()


# def person(name, *args):
#     # *args returns other values in tuple
#     print(name)
#     print(args)


# person("Tushar", age=25, city="Mumbai", current_status="Searching somone")
# We can't pass value like these and access by defining variable
# Insted use **kwargs that are in dictionary

def person(name, **args):

    print(name)
    print(args)


person("Tushar", age=25, city="Mumbai", current_status="Searching somone")
# **args above return all the assigned values in the dictionary format
