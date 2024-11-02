#var 1

def polindrom (number = 123321):
    """palindrome search function"""
    number = str(number)

    mas_reverse = []
    mas = []

    for letter in number:
        mas.append(letter)
        mas_reverse.append(letter)

    mas_reverse.reverse()

    if mas == mas_reverse:
        return True
    else:
        return False

result = polindrom()

print(result)

#var 2 "mathematical solution"

def is_polindrom (number = -546645):
    """palindrome search function"""
    if number < 0:
        number = abs(number) #check for a negative number and its inerting
        #or return False

    origin_number = number
    reverse_number = 0

    while number > 0:
        last_digit = number % 10
        reverse_number = reverse_number * 10 + last_digit
        number //= 10

    if origin_number == reverse_number:
        return True
    else:
        return False

result = is_polindrom()

print(result)



