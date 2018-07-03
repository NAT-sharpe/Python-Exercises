# $ python guess_the_number.py
# I am thinking of a number between 1 and 10.
# What's the number? 3
# Nope, try again.
# What's the number? 9
# Nope, try again.
# What's the number? 5
# Yes! You win!

print 'I am thinking of a number between 1 and 10...'

right_num = 4

while True:
    num = input('What\'s the number? ')
    guess = num
    if guess == right_num:
        print 'Yes! you win!'
        break
    else:
        print 'Nope. Try again'
        

        




