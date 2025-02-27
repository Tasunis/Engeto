""""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Vojtěch Otruba
email: voj..otruba@gmail.com
"""
""" #login verification
class UserVerification:
    username = input("username: ")
    password = input("password: ")
    print("-" *40)
    #names and passwords tuples
    userList = ("bob", "ann", "mike", "liz")
    passwordList = ("123", "pass123", "password123", "pass123")
    #username verification
    if username not in userList:
        print("Unregistered user, terminating program...")
        exit()
    else: #password verification
        a = userList.index(username) 
        if password != passwordList[a]: #nonregistered user
            print("Wrong password, terminating program...")
            exit()
        else: #registered user
            print("Welcome to the app,", username)  """
#text division 
class AnalyzeText:
    divider = ("-" *40)
    print(divider)
    #texts
    TEXTS = ['''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley. ''',
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
    text = ("")
    #text choice
    textNumber = int(input(f"{"Please select your text(1-"}{maxText}{"):"} "))
    print(divider)
    if (textNumber == 1):
        analyzedText = TEXTS[0]
        text = TEXTS[0]
    elif (textNumber == 2):
        analyzedText = TEXTS[1]
        text = TEXTS[1]
    elif (textNumber == 3):
        analyzedText = TEXTS[2]
        text = TEXTS[2]
    else: 
        print("Not possible, terminating...")
        exit()
    #division of text to words
    chosenText = ""
    for line in text:
        chosenText = chosenText + line.strip(".,\n")   
    words = [word for word in chosenText.split() if word]
    #number of words
    wordAmount = len(words)
    print("There are", wordAmount, "words in the selected text.")
    #number of titlecase words
    wordsInTitle = 0
    for word in words:
        if word.istitle():
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
    #number of numeric strings
    numericStrings = 0
    for word in words:
        if word.isnumeric():
            numericStrings += 1
        else:
            continue
    print("There are", numericStrings, "numeric strings.")
    #sum of all numbers
    sumOfTextNumbers = 0
    for sum in words:
        if sum.isdigit():
            sumOfTextNumbers = int(sumOfTextNumbers) + int(sum)
        else:
            continue
    print("The sum of all the numbers is", int(sumOfTextNumbers))
    #word length analysis
    lengthCounts = {}
    for word in words:
        length = len(word)
        lengthCounts[length] = lengthCounts.get(length, 0) + 1
    #graph
    print(divider)
    print(f"{'LEN|' : >5}{'OCCURENCES' : ^15}{'|NR.' : >5}")
    print(divider)
    for length in sorted(lengthCounts):
        print(f"{length : >3} |{'*' * lengthCounts[length] : <15} |{lengthCounts[length]}")