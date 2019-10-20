import re

#patterns = ["term1", "Term2"]

text = "This is a string with term1, not not the other"

#for pattern in patterns:
    #print ("I'm searching for: " + pattern)

    #if re.search(pattern,text):
       # print ("Match!!")


    #else:
        #print ("No Match")


#match = re.search("term1",text)

#print (match.start())



#split

#split_term = '@'

#email = 'Kennedy@gmail.com'

#print (re.split(split_term,email))


#Find instances of a pattern

#print (re.findall('match', 'test phrase match in match middle'))



#Medi character syntax


def mult_re_find(patterns,phrase):

    for pat in patterns:
        print ("Srarching for pattern {}".format(pat))
        print(re.findall(pat,phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

#test_phrase ='sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

#test_patterns = ['sd*']

#test_patterns = ['sd+']

#count
#test_patterns = ['sd{1,3}']

#start with letter s and more ds
#test_patterns = ['[sd]+']

test_patterns = ['[^!.?]+']

mult_re_find(test_patterns,test_phrase)