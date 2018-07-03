def add_numbers(list_of_numbers):
    number = 0
    for each in list_of_numbers:
        number += each
    return number

list_of_numbers = [10, 9, 33, 40]

result = add_numbers(list_of_numbers)

print result

