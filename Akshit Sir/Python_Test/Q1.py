# size_of_list = int(input("Enter the size of the list: "))
# list_of_element = []
# for i in range(0, size_of_list):
#     element_of_list = int(input("Enter the element: "))
#     list_of_element[i] = element_of_list

list = [3, 4, 5, 1, 2]
list = [1, 2, 3]


def solution():
    for i in range(0, len(list)):
        if (i < len(list)):
            if (i == len(list)):
                if (list[len(list)] > list[i]):
                    i = 0
                if (list[i+1] > list[i]):
                    continue
        if (list[i-1] > list[i]):
            continue
        return True
    else:
        return False


a = solution()
print(a)
