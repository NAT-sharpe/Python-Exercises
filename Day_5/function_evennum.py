def even_numbers(list_of_numbers):
    even = []
    for each in list_of_numbers:
        if each % 2 == 0:
            even.append(each)
    return even

list_of_numbers = [10, 9, 33, 40]

result = even_numbers(list_of_numbers)

print result







