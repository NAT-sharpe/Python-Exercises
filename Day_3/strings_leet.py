message = "STORM THE CASTLE!"
leet_message = ""

uppercase = "AEGIOST"
leet = "4361057"


for char in message:
    for i in range(len(uppercase)):
        change = uppercase[i]
        if change == char:
            char = leet[i]
            break

    leet_message = leet_message + char

print leet_message