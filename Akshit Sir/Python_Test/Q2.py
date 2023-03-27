# list = [0, 1, 0, 0, 1, 1, 0, 1]

# for i in list:
#     # print(list)
#     if (list[i-1] > list[i]):
#         temp = list[i]  # temp = 0
#         list[i+1] = list[i]
#         temp = list[i+1]
# print(list)

list = [0, 1, 0, 0, 1, 1, 0, 1]
list.sort()
print(list)


def swap():
    list = [0, 1, 0, 0, 1, 1, 0, 1]
    # starting part of list
    for i in range(0, len(list), 1):
        # last part of list
        for j in range(len(list), -1):
            if (list[i] > list[j]):
                temp = list[i]  # temp = 0
                list[j] = list[i]  # storing variable of j into i
                temp = list[j]
            elif (list[j] > list[i]):
                temp = list[j]  # temp = 0
                list[i] = list[j]  # storing variable of j into i
                temp = list[i]  # storing i list element into temp
            elif (list[i] == list[j]):
                break


print(list)

swap()
