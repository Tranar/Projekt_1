"""                                                        
projekt_1.py: první projekt do Engeto Online Python Akademie 

author: Lukáš Lajda
email: llajda@seznam.cz
"""                                                         #požadovaná hlavička

TEXTS = [                                                   #zadaný text
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

users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}   #slovník uživatelů a hesel
separator = "-"*35                                                              #oddělovač
first_text = tuple(TEXTS[0].split())                                            #první část textu převede po slovech na tuple
second_text = tuple(TEXTS[1].split())                                           #druhá část textu převede po slovech na tuple
third_text = tuple(TEXTS[2].split())                                            #třetí část textu převede po slovech na tuple

def analyze_text(part):                                             #vlastní příkaz na analýzu textu
    number_words = len(part)                                        #spočítá počet slov v textu
    istitled = 0                                                    #nastaví hodnotu proměnné na 0 
    
    for word in part:                                               #projde každé slovo v textu
        if word.istitle():                                          #pokud slovo začíná velkým písmenem
            istitled += 1                                           #tak k proměnné přičte 1

    print(f"""There are {number_words} words in the selected text. 
    There are {istitled} titlecase words.
               """)                                                 #provede výpis analýzy
    

username = input("username: ")
password = input("password: ")
print(separator)

if username in users and users[username] == password:       #kontroluje shodu uživatelů a hesel
    print(f"""Welcome to the app, {username}     
We have 3 texts to be analyzed.""")
    print(separator)
    vyber_textu = input("Enter the number btw. 1 and 3 to select: ")    #vstup s výběrem textu k analýze
    if vyber_textu == "1":
        analyze_text(first_text)
    elif vyber_textu == "2":
        print(second_text)
    elif vyber_textu == "3":
        print(third_text)
    else:
        print("This choice is not allowed.")

else:
    print(f"unregistered user, terminating the program..")


