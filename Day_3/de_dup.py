my_list = [1, 3, 5, 3, 2, 4, 2, 1, 4]
new_list = []

# for num in my_list:
#     for i in range(len(new_list)):
#         if num in new_list:
#             break
#         else:
#             new_list.append(num)

# print new_list

for num in my_list:
    if num not in new_list:
        new_list.append(num)

print new_list


# print new_list

# for num in my_list:
#     while num in new_list != False:
#         new_list.append(num)

# print new_list