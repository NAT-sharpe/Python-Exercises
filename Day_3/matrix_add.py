box_a = [[1, 3], [2, 4]]

top_a = box_a[0]
bot_a = box_a[1]


box_b = [[5, 2], [1, 0]]

top_b = box_b[0]
bot_b = box_b[1]

top_left = top_a[0] + top_b[0]
top_right = top_a[1] + top_b[1]
bot_left = bot_a[0] + bot_b[0]
bot_right = bot_a[1] + bot_b[1]


box_c = [[top_left, top_right], [bot_left, bot_right]]

answer = "%s %s \n%s %s" % (top_left, top_right, bot_left, bot_right)

print answer
