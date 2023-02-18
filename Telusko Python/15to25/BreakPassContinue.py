# x = int(input("How many candies due to need? "))
# i = 1
# av = 10
# for i in range(1, x+1, 1):
#     if (i > av):
#         print("Out of Stock")
#         break
#     print("Candy")
# print("Bye")

for i in range(1, 101, 1):
    if i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue
    print(i)


def passDemo():
    print("Hii how are u buddy? ")
    pass


passDemo()
