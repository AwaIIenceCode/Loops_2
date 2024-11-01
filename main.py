def _min_of_five(num_1 = 3, num_2 = 7, num_3 = -3, num_4 = 0, num_5 = 11):
    numbers = [num_1, num_2, num_3, num_4, num_5]
    my_min_of_five = numbers[0]

    for number in numbers:
        if number  < my_min_of_five:
            my_min_of_five = number

    print(my_min_of_five)

_min_of_five()

# The second option is for the crazies :)

# def _min_of_five(num_1 = 8, num_2 = 3, num_3 = 1, num_4 = -2, num_5 = 0):
#     if num_1 < num_2 and num_1 < num_3 and num_1 < num_4 and num_1 < num_5:
#         print(num_1)
#     elif num_2 < num_1 and num_2 < num_3 and num_2 < num_4 and num_2 < num_5:
#         print(num_2)
#     elif num_3 < num_1 and num_3 < num_2 and num_3 < num_4 and num_3 < num_5:
#         print(num_3)
#     elif num_4 < num_1 and num_4 < num_2 and num_4 < num_3 and num_4 < num_5:
#         print(num_4)
#     else:
#         print(num_5)
#
# _min_of_five()