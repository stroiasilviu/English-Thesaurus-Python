# English Dictionary V2

import json
from difflib import get_close_matches

with open("dict_data.json", "r") as f:
    data = json.load(f)


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y if yes, or N if no: ")
        if yn == "y" or "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n" or "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter a word: ")
output = translate(word)

if type(output) is list:
    for element in output:
        print(element)
else:
    print(output)
