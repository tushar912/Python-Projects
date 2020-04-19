import json
from difflib import get_close_matches
data =json.load(open("original.json"))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.key()))> 0:
        print("Did you mean",get_close_matches(word,data.key())[0])
        i=input("press y or n")
        if i=='y':
            return data[get_close_matches(word,data.key())[0]]
        elif i=='n':
            print("wrong input")
        else:
            print("wrong input")
    else:
        print("wrong input")
word = input("Enter the word")
o = translate(word)
if type(o)==list:
    for i in o:
        print(i)
else:
    print(o)
