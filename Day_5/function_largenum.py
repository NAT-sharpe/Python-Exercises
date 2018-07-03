def big_number(list_of_numbers):
    big = list_of_numbers[0]
    for number in list_of_numbers:
        if number > big:
            big = number
    return big

list1 = '6327280'

result = big_number(list1)

print result

