# Sentence = input("Enter a sentence: ")
# x = " "
# length_of_sentence = len(Sentence)
# print("There are", length_of_sentence, "characters in your name.")
# print("The number of times 'A' occurs in your name is: ", Sentence.count('a'))
# print("The number of times 'E' occurs in your name is: ", Sentence.count('e'))
# print("The number of times 'I' occurs in your name is: ", Sentence.count('i'))
# print("The number of times 'O' occurs in your name is: ", Sentence.count('o'))
# print("The number of times 'u' occurs in your name is: ", Sentence.count('u'))


def find_Vowels():
    Sentence = input("What is your name: ")
    count_of_a = 0
    count_of_e = 0
    count_of_i = 0
    count_of_o = 0
    count_of_u = 0
    for char in Sentence:
        a = char
        print(a)
        if (a == 'a' or a == 'A'):
            count_of_a += 1
        if (a == 'e' or a == 'E'):
            count_of_e += 1
        if (a == 'i' or a == 'I'):
            count_of_i += 1
        if (a == 'o' or a == 'O'):
            count_of_o += 1
        if (a == 'u' or a == 'U'):
            count_of_u += 1
    print(f"There are {len(Sentence)} characters in your name. ")
    print("The number of times 'A' occurs in your name is", count_of_a)
    print("The number of times 'E' occurs in your name is", count_of_e)
    print("The number of times 'I' occurs in your name is", count_of_i)
    print("The number of times 'O' occurs in your name is", count_of_o)
    print("The number of times 'U' occurs in your name is", count_of_u)


find_Vowels()
