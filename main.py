"""An interactive cli dictionary"""

#modules
import json
import difflib


#load dict json
data = json.load(open("data.json"))

#how i intend to keep the app running
valuePassed = 0

#funtion to return translation
def getMeaning(word, data,):
    index = 1
    result = ""
    for meaning in data[word]:
        result += "%s %s: %s \n" % (word, str(index), meaning)
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
        confirm = raw_input("Did you mean %s? Enter Y for yes and N for no:\n" % possible_match)
        
        if confirm.lower() == "y":
            result =  getMeaning()(possible_match, data)

        elif confirm.lower() == "n":
            result = "%s doesn't exist in our DB?" % word

        else:
            result = "Query not clear"

    else:
        result = "%s doesn't exist in our DB?\n\n" % word

    return result

#accept input from user
while valuePassed != 1:
    query = raw_input("Enter word: ")
    #make query case insensitive
    query = query.lower()

    #print input
    print(getDefinition(query))