answer = 'yes'

coins = 0

while answer == 'yes':
    total = 'You have %s coins.' % coins    
    print total   
    answer = raw_input('Do you want another? ')
    coins += 1
    if answer == 'no':
        print 'Bye'

 