def small_number(list_of_numbers):
    small = list_of_numbers[0]
    for each in list_of_numbers:
        if each < small:
            small = each
    return small

list1 = [-1, 10, 9, 33, 40]

result = small_number(list1)

print result







