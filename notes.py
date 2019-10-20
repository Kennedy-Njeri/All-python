try:

    f = open('simple.txt', 'r')
    f.write("Test write to simple text!")

#No need to specify type of error
except IOError:
    print ("Error: Could Not Find Or Read Data")

else:
    print ("Success")
    f.close()


#If You want The error To continue

try:

    f = open('simple.txt', 'r')
    f.write("Test write to simple text!")

#No need to specify type of error
except IOError:
    print ("Error: Could Not Find Or Read Data")

finally:
    print ("Success")
    f.close()