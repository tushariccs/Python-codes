#Dictionary: key-value pair,unordered,mutable
#initializ 01
user_details = {
    "name":"Mona darling",
    "age":22,
    "area":"Wednesday"
}
print(user_details["age"])

#initialize 02
new_user_details=dict(name="Priyanka",age="22")
print(new_user_details)

#add new key pair
user_details["amt"] = 6000
print(user_details)
'''
#new value to key
user_details["name"] = "Ocean"
print(user_details)

#delete
del user_details["amt"]
print("after deletion",user_details)

#delete by pop
age = user_details.pop("age")
print(age)
print(user_details)

#popitem
user_details.popitem()
print(user_details)
'''
#check key is in dictionary
key = "amount"
if key in user_details:
    print("key found")
else:
    print("key not found")


#retrieve
for key in  user_details:
    print(key)
    print(user_details[key])
    
#keys

#values


#updates
update_details = {"name":"Ocean","age":27,"gender":"Female"}
user_details.update(update_details)
print(user_details)

