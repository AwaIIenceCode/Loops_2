#var 1
def polindrom (number = 123321):
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