while True:
    start = input("Start from: ")
    end = input("End on: ")

    if start < end:
        for i in range(start,end + 1):
            print i
        break

    else:
        print "Start must be greater than End!"
       

    
