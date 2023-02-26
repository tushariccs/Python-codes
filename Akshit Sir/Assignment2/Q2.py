in_string = input("Enter a sentence: ")
list = in_string.split(" ")
print(list)
search_element = input("The element to be searched: ")
count_of_word = 0

for list_items in list:
    if (list_items == search_element):
        count_of_word += 1
    else:
        continue

print("How many times the search word appears in the string.", count_of_word)
