def multply(list_of_numbers, factor):
    new_list = []
    for each in list_of_numbers:
        product = each * factor
        new_list.append(product)
    return new_list

list_of_numbers = [10, 9, 33, 40]
factor = 4

result = multply(list_of_numbers, factor)

print result