def all_even_numbers_between_them (num_1, num_2):
    for i in range(num_1, num_2):
        if i % 2 == 0:
            print(i, end = " | ")

all_even_numbers_between_them(2,50)