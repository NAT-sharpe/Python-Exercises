# def find_postive_numbers(list_of_numbers):
#     positive = []
#     for each in list_of_numbers:
#         if each > 0:
#             positive.append(each)
#     return positive

def print_positive_num(n):
    pos_numbers = []
    for i in n:
        if i > 0:
            pos_numbers.append(i)

    return pos_numbers

list_of_numbers = [-1, 0, 10, 9, 33, -40]

result = print_positive_num(list_of_numbers)

print result

# def find_postive_numbers(list_of_numbers):
#     for each in list_of_numbers:
#         if each > 0:
#             print each

# list_of_numbers = [-1, 0, 10, 9, 33, 40]

# result = find_postive_numbers(list_of_numbers)





