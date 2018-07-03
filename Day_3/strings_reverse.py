message = "storm the castle!"

message_reverse = ""

for i in range(len(message)):
    letter = message[-i-1]
    message_reverse += letter

print message_reverse