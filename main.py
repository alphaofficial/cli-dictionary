"""An interactive cli dictionary"""

#modules
import json
import difflib


#load dict json
data = json.load(open("data.json"))

#function to lookup a word in the dict
def getDefinition(word):
    result = ""
    index = 1
    if word in data:
        if len(data[word]) > 1:
            for meaning in data[word]:
                result += "Result "+ str(index) +": " + meaning + "\n"
                index = index + 1
        else:
            result = data[word]
    else:
        #find matches in DB
        #get_close_matches will return matches in order of similarity. So obviously first word is a possible match
        possible_match = difflib.get_close_matches(word, data.keys())[0]
        
        result = word + " doesn't exist in our DB. Did you mean " + possible_match + "?"

    return result

#accept input from user
query = raw_input("Enter word: ")
#make query case insensitive
query = query.lower()

#print input
print(getDefinition(query))