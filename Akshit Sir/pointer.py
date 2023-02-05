def sum_of_numbers(number_01,*numbers_02):
    result = number_01 + sum(numbers_02)
    print(result)

sum_of_numbers(10,20,30,40,50)