class AnalyzeText:
    divider = "-" *35
    print(divider)
    
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

    text = ("")
    """ for line in TEXTS:
        text = text + line
    splitText = text.split("'''") """
    while True:
        textNumber = int(input("Please select your text(1-3): "))
        
        if (textNumber == 1):
            analyzedText = TEXTS[0]
            print(TEXTS[0])
            text = TEXTS[0]
            break
        elif (textNumber == 2):
            analyzedText = TEXTS[1]
            print(TEXTS[1])
            text = TEXTS[1]
            break
        elif (textNumber == 3):
            analyzedText = TEXTS[2]
            print(TEXTS[2])
            text = TEXTS[2]
            break
        else:
            print("Please select your text(1-3): ")
    """ stringToList = analyzedText.split() """
    """ print(stringToList) """
    text1 = ""
    for line in text:
        text1 = text1 + line.strip(".,\n")
    
    print(text)
   
    print(text1)
    
    words = [word for word in text1.split() if word]
    print(words)