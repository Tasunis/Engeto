""""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Vojtěch Otruba
email: voj.otruba@gmail.com
"""
#login verification
def verification(username, password):
    if username not in userList:
        print("Unregistered user, terminating program...")
        exit()
    else:  # password verification
        a = userList.index(username)
        if password != passwordList[a]:  #nonregistered user
            print("Wrong password, terminating program...")
            exit()
        else:  # registered user
            print("Welcome to the app,", username)
#names and passwords tuples
userList = ("bob", "ann", "mike", "liz")
passwordList = ("123", "pass123", "password123", "pass123")
#login input
username = input("username: ")
password = input("password: ")
print("-" *40)
verification(username, password)
#text division 
divider = ("-" *40)
#texts
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
maxText = len(TEXTS)
print("We have", maxText, "texts to analyze.")
print(divider)
text = ""
#input verification
try:
    textNumber = int(input(f"{'Please select your text(1-'}{maxText}{'):'} "))
    if textNumber > maxText or textNumber <= 0:
        raise ValueError
except ValueError:
        print("Not possible, terminating...")
        exit()
#text choice
print(divider)
chosenText = TEXTS[textNumber - 1]
#division of text to words
words = [word.strip(",.") for word in chosenText.split() if word]
#number of words
wordAmount = len(words)
print("There are", wordAmount, "words in the selected text.")
#number of titlecase words
wordsInTitle = 0
for word in words:
    if word.istitle():
        if word.isalpha():
            wordsInTitle += 1
print("There are", wordsInTitle, "titlecase words.")
#number of uppercase words
wordsInCaps = 0
for word in words:
    if word.isupper():
        if word.isalpha():
            wordsInCaps += 1
        else:
            continue
print("There are", wordsInCaps, "uppercase words.")
#number of lowercase words
wordsInLowercase = 0
for word in words:
    if word.islower():
        wordsInLowercase += 1
print("There are", wordsInLowercase, "lowercase words.")
#number of numeric strings and sum of all numbers
numericStrings = 0
sumOfTextNumbers = 0
for word in words:
    if word.isnumeric():
        numericStrings += 1
        sumOfTextNumbers += int(word)
    else:
        continue
print("There are", numericStrings, "numeric strings.")
print("The sum of all the numbers is", int(sumOfTextNumbers))
#word length analysis
lengthCounts = {}
for word in words:
    length = len(word)
    lengthCounts[length] = lengthCounts.get(length, 0) + 1
#graph
print(divider)
print(f"{'LEN|' : >5}{'OCCURENCES' : ^17}{'|NR.' : >5}")
print(divider)
for length in sorted(lengthCounts):
    print(f"{length : >3} |{'*' * lengthCounts[length] : <17} |{lengthCounts[length]}")