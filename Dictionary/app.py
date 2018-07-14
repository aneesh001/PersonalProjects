import json
from difflib import get_close_matches


def translate(word, data):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        matches = get_close_matches(word, data.keys())

        if len(matches) > 0:
            yn = input("Did you mean %s instead? Enter Y is yes, or N if no: " % matches[0])
            if yn == 'Y':
                return data[matches[0]]

        return "The word doesn't exist. Please double check it."


data = json.load(open("data.json", "r"))
word = input("Enter a word: ")
output = translate(word, data)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
