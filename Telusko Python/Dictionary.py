# phone_numbers = {
#     1:"Tushar Nitin Bhansali",
    
# }

data = {1:'Navin',2:'Kiran',3:'Harsh'}
print(data)

print(data[3])
print(data[1])
print(data.get(1))
print(data.get(1,'Not Found'))
#If there no index found then second parameter is used for key not found
print(data.get(4,'Not Found'))

keys = ['Navin','Kiran','Harsh']
values = ['Navin loves python','Java','JavaScript']

data  = dict(zip(keys,values))
print(data)
# data  = (zip(keys,values))
# print(data)
result = data['Kiran']
print(result)
#adding a value
data['Monika'] = 'C#'
print(data)

prog = {'JS':'Atom','C#':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'NetBeans','JEE':'Eclipse'}}
print(prog)

print(prog['Python'][1])
