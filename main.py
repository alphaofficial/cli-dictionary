"""An interactive cli dictionary"""

#modules
import json
import difflib

#load dict json
data = json.load(open("data.json"))


#funtion to return translation
def getMeaning(word, data,):
    index = 1
    result = ""
    for meaning in data[word]:
        result += "%s %s: %s \n\n" % (word, str(index), meaning)
        index = index + 1
    return result

#function to lookup a word in the dict
def getDefinition(word):
    result = ""
    if word in data:
        result = getMeaning(word, data)

    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        #get_close_matches will return matches in order of similarity. So obviously, the first word is a possible match
        possible_match = difflib.get_close_matches(word, data.keys())[0]
        confirm = input("Did you mean %s? Enter Y for yes and N for no:\n\n" % possible_match)
        
        if confirm.lower() == "y":
            result =  getMeaning(possible_match, data)

        elif confirm.lower() == "n":
            result = "%s doesn't exist in our DB?\n\n" % word

        else:
            result = "Query not clear\n\n"

    elif word == "":
        result = "You entered nothing\n\n"

    else:
        result = "%s doesn't exist in our DB?\n\n" % word

    return result


######################################################################################
"""Intro to run app"""

print("***Welcome to interactive dictionary***\nSimply enter a word you'd like to look up and get the meaning or translation!\n\n\n")

#Persist input from user
while True:
    query = input("Enter word: ")
    #make query case insensitive
    query = query.lower()

    #print input
    print(getDefinition(query))