# class Item:
#     def __init__(self, name, price, qty):
#         self.name = name
#         self.price = price
#         self.qty = qty

#     def calculate_total_price(self):
#         return self.price * self.qty


# phone = Item("Phone", 1000, 2)
# print(phone.name, phone.price, phone.qty)

# default value is only given to last parameter of the arg
# If u give in between then u need to assign default value to all further remaining parameters


#    def __init__(self, name, price:float, qty):
#         self.name = name
#         self.price = price
#         self.qty = qty


# to define a datatype for an parameter in constructor function

#    def __init__(self, name, price:float, qty=1):
#         self.name = name
#         self.price = price
#         self.qty = qty


class Item:
    def __init__(self, name: str, price: float, qty: int = 1):
        self.name = name
        self.price = price
        self.qty = qty

    def calculate_total_price(self):
        return self.price * self.qty


Laptop = Item("Asus", 200000.0, 6)
print(Laptop.calculate_total_price())

# u can change the value of last parameter i.e qty but if no define it then it will 1 by default


class Item:
    all = []

    def __init__(self, name: str, price: float, qty: int = 1):
        self.name = name
        self.price = price
        self.qty = qty
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.qty

    def __repr__(self) -> str:
        return "f", {Item.all}


Laptop = Item("Asus", 200000.0, 6)
print(Laptop.calculate_total_price())
earphone = Item("Earphone", 200, 2)
Charger = Item("Charger", 20, 2)

# for items in Item.all:
#     print(items)


# def __repr__ is used for representation
