def digit_count(number = 3456):
    count_numbers = 0

    while number != 0:
        number //= 10
        count_numbers += 1

    return count_numbers

result = digit_count()

print(result)