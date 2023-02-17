# decleration
def function_name(args01, arg02):
    pass

# no arg,no return


def greeting():
    print("Good Morning")


greeting()

# no arg,return


def afternoon_wish():
    return "Good afternoon! "


# wish = afternoon_wish()
# print(wish)
print(afternoon_wish())

# arg,no return


def evening_wish(name):
    print(f"Good evening{name}")


evening_wish(" Tushar!")

# arg return


def night_wish(name):
    return f"Good night", {name}


night_greeting = night_wish("Tushar")
print(night_greeting)
