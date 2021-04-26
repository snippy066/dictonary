import json

data=json.load(open("C:\\Users\\Snippy066\\Downloads\\data.json"))

def definition(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("Sorry!! this word doesn't exist in dictionary...")

while True:
    word=input("please enter the word :")
    out=definition(word)

    print(out)
    key=input("if you want to continue press y \n if you want to quit press any key :")
    if(key=='y'):
        continue
    else:
        print("you quited the game Thank you for playing :)")
        break
    
        