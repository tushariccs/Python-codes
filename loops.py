counter = 0 
# while counter<10:
#     print(counter)
#     counter+=1

# print("\n")    
# numbers = [0,10,20,30,40,50,60,70,80,90]
# for number in numbers:
#     print(number)
    
    
# number = list(range(0,20,2))
# print(number)

# number = list(range(0,20,3))
# print(number)


# number = list(range(20,0,-3))
# print(number)


# while True:
#     print(counter)
#     counter+=1


# for number in range(10):
#     print(number)

# for number in range(10):
#     for times in range(number):
#         print(number,end="")
#     print()


# print("Hello world ",end="whatever ")
# print("\nHow are u?")


for increment in range(1, 4,-1):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for justify in range(1, increment+1):
         
            # printing stars
            print(justify,end="")
      
        # ending line after each row
        print("\r")