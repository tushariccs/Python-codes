# String:ordered,immutable,text representation

# init
series_name = "The Woman in the House Across the Street from the Girl in the Window"
web_series = ("Suits", "You", "Friends")
print(series_name)
print(web_series)

series_name = "Game of Thrones"
web_series = ("GOT", "HIMYM")
print(series_name)
print(web_series)

# single quote
fav_quote = 'That\'s what she said'
print(fav_quote)

# double quote
fav_quote = "That's what she said"
print(fav_quote)

# triple quote

quote = """Where should I go?
To the left where nothing is right
to the right where nothing is left"""
print(quote)
web_series = ["GOT", "HIMYM", "Suits", "Friends", "You", "Elite"]
print(web_series[2:5])

print(web_series[3:0:-1])  # To access element in reverse manner
# indexing
# To access element in reverse manner
print(quote[0])
print(quote[-1])
print(fav_quote[7:15])

# reverse string
print(fav_quote[::-1])

# slicing
fav_quote = "That's what she said"
web_series = ["GOT", "HIMYM", "Suits", "Friends", "You", "Elite"]
# last variable
print(fav_quote[-1])
print(fav_quote[10:6:-1])
print(web_series[3:0:-1])

# concatenate
greeting = "Good Morning"
name = " John Doe"
greeting = greeting + name
print(greeting)

# interation
for char in name:
    print(char)

# check
print("Morning" in greeting)

# white spaces
hello = "    hello".strip()
print(hello)

# upper and lower
print(hello.upper())

username = "TusHARiCCSSSsss"
print(username.lower())

# startswith
akshit_email = "akshit.mathiwala@techbulls.com"
tushar_email = "techbullstushar"
aditya_email = "techbullsaditya"

print(tushar_email.startswith("techbulls"))
print(akshit_email.endswith("techbulls.com"))

# find
akshit_name = "mathaiwalaakshit"
# to find index value of the character
print(akshit_email.find("a"))
# if character is not found it will return -1

# SHIT
s_index = akshit_name.find('s')
print(s_index)
splited_name = akshit_name[s_index:]
print(splited_name)
upper_splited_name = splited_name.upper()
print(upper_splited_name)
# AKSHIT
# to find shit in name in upper case


# count
series_name = "The Woman in the House Across the Street from the Girl in the Window"
print(series_name.count("e"))

# replace
print(series_name.replace("the", "anything"))
print(series_name)


# split
print(series_name)
print(series_name.split(" "))
print(series_name.split(","))
print(series_name.split("e"))
splited_string_list = series_name.split()
print(series_name)

# join
joining_list = ",".join(splited_string_list)
print(joining_list)


# if we don't use join and split and we want this o/p \
# The,Woman,in,the,House,Across,the,Street,from,the,Girl,in,the,Window
# then use replace(" ",",")

a_list = ['a']*10
print(a_list)
a_list = "".join(a_list)
print(a_list)
# print(a_list.replace(",", ""))

# another method to that
a_string_2 = ""
for a in a_list:
    a_string_2 += a
print(a_string_2)

# % .format() f-string
greeting = "Good Morning,"
name = " John Doe"
print(greeting + " "+name)
print("{}whatever {} adads".format(greeting, name))
print(f"{greeting}adadss{name}vikier{10+30}")
