start = input("Start from: ")
end = input("End on: ") + 1

if end < start:
    print "Sorry, 2nd number must be greater than 1st."
    start
    end    
for i in range(start,end):
    if end < start:
        print "End must be greater than start"
    print i
    
