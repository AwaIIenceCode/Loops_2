# var 1
# def product_diapazone (num_1 = 25, num_2 = 5):
#     """function multiplies numbers in the range"""
#     product = 1
#
#     if num_1 < num_2:
#         for num in range (num_1, num_2 + 1):
#             product *= num
#         print(product)
#
#     else:
#         num_1, num_2 = num_2, num_1
#         for num in range (num_1, num_2 + 1): #the values num_1 and num_2 of the variables can not be changed, but simply swap num_1 and num_2 in the stipulation loop
#             product *= num
#         print(product)
#
# product_diapazone()

# var 2
def product_diapazone (num_1 = 25, num_2 = 5):
    """function multiplies numbers in the range"""
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1

    product = 1

    for num in range (num_1, num_2 + 1):
        product *= num

    return product

result = product_diapazone()

print(result)

# In this variant I shortened and improved the code, and also corrected the problem condition,
# where it was said that it was necessary to return and not to output the result.