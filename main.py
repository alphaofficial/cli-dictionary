"""An interactive cli dictionary"""
import json

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
        result = word + " doesn't exist in our DB"

    return result

#accept input from user
query = raw_input("Enter word: ")
#make query case insensitive
query = query.lower()

#print input
print(getDefinition(query))