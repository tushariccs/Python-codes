# samsung_name = "Samsung S20 FE 5g"
# samsung_price = 50000
# samsung_qty = 10
# samsung_total_amount = samsung_price * samsung_qty
# print(samsung_total_amount)

# iphone_name = "Samsung S20 FE 5g"
# iphone_price = 72000
# iphone_qty = 5
# iphone_total_amount = iphone_price * iphone_qty
# print(iphone_total_amount)


# class Product:
#     pass


# samsung = Product()
# print(type(samsung))


class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def calculate_total_amount(self):
        return self.price * self.qty


samsung = Product("Samsung FE", 50000, 10)
iphone = Product("Iphone 14 Pro Max", 72000, 5)
print(samsung.name)
print(samsung.calculate_total_amount())
print(iphone.calculate_total_amount())
