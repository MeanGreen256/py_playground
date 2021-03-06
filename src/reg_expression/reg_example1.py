#!/usr/bin/python
import re

def match_example():
    #match function
    line = "Cats are smarter than dogs"

    matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

    if matchObj:
        print("test", matchObj.group())
        print("matchObj.group(1) : ", matchObj.group(1))
        print("matchObj.group(2) : ", matchObj.group(2))
    else:
        print ("No match!!")

def search_example():
    #search function
    line = "Cats are smarter than dogs"

    searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

    if searchObj:
        print("searchObj.group() : ", searchObj.group())
        print("searchObj.group(1) : ", searchObj.group(1))
        print("searchObj.group(2) : ", searchObj.group(2))
    else:
        print("Nothing found!!")

#main
match_example()
search_example()