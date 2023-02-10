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
print(fav_quote[10:6:-1])
print(web_series[3:0:-1])
