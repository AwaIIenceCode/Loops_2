def print_square (symbol, side, variation):
    if variation == True:
        for i in range (side):
            print((symbol + ' ') * side) # I'm using + ' ' it to make the square more readable
    elif variation == False:
        for i in range (side):
            if i == 0 or i == side - 1:
                print(symbol * side )
            else:
                print(symbol + ' ' * (side - 2) + symbol)
    else:
        print('Invalid variation, try again')

print_square('*',5,True)
