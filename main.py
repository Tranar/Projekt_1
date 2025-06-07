"""                                                        
projekt_1.py: první projekt do Engeto Online Python Akademie 

author: Lukáš Lajda
email: llajda@seznam.cz
"""                                                         #požadovaná hlavička

TEXTS = [                                                   #analyzovaný text
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
separator = "-" * 45                                                            #oddělovač

def analyze_text(part):                                             #vlastní funkce na analýzu textu
    part = [word.replace(",", "") for word in part]                 #očistí list od ,
    part = [word.replace(".", "") for word in part]                 #očistí list od . 
#bylo mi jasné, že výše uvedené dva příkazy lze udělat i jednodušeji, ale to mi už musela poradit AI part = [word.replace(",", "").replace(".", "") for word in part]        
    number_words = len(part)                                        #spočítá počet slov v textu
    word_istitle = 0                                                #nastaví hodnotu proměnné na 0 
    word_isupper = 0                                                #nastaví hodnotu proměnné na 0
    word_islower = 0                                                #nastaví hodnotu proměnné na 0
    word_isnumeric = 0                                              #nastaví hodnotu proměnné na 0
    word_numeric = []                                               #vytvoření prázdného seznamu pro číselné hodnoty
    num_letters = []                                                #vytvoření prázdného seznamu pro číselné hodnoty, počet písmen v každém slově

    for word in part:                                               #projde každé slovo v textu
        if word.istitle():                                          #pokud slovo začíná velkým písmenem
            word_istitle += 1                                       #tak k proměnné přičte 1
        elif word.isupper():                                        #pokud je celé slovo velými písmeny
            word_isupper +=1
        elif word.islower():                                        #pokud je slovo malými písmeny
            word_islower += 1
        elif word.isnumeric():                                      #pokud slovo je vyjádření čísla
            word_isnumeric += 1
            word_numeric.append(int(word))                          #naplnění seznamu word_numeric číselnými hodnotami
    
    sum_numeric = sum(word_numeric)                                 #součet číselných hodnot seznamu word_numeric

    print(f"""There are {number_words} words in the selected text. 
There are {word_istitle} titlecase words.
There are {word_isupper} uppercase words.
There are {word_islower} lowercase words.
There are {word_isnumeric} numeric strings.
The sum of all the numbers {sum_numeric}""")                        #provede výpis analýzy
    print(separator)
    print("LEN", "\tOCCURENCES\t", "NR.", sep="|")                  #vytiskne záhlaví grafické části
    print(separator)
 
    for word in part:                                               #část kódu věnující se výpočtu hodnot pro grafickou část
        num_letters.append(str(len(word)))                          #připojí do prázdného seznamu počet písmen každého slova
    
    for number in range(1,20):                                      #cyklus v určitém rozsahu, kdy každý cyklus reprezentuje slovo o jedné pozici
        occurence = num_letters.count(str(number))                  #proměnná occurence ukládá množství výskutu slov o daném počtu pozic
        occurence_graphic = "*" * occurence                         #proměnná occurence_graphic znázorňuje graficky totéž co occurence
        gap = " " * (25 - occurence)                                #nastavení pohyblivé mezery dle množství výskutu slov o daném počtu pozic
        if occurence:
            print(f"{number:>3}| {occurence_graphic}{gap}| {occurence}") #tisk grafického výstupu, použití zarovnání vpravo šířka 3 a vložení plovoucí mezery "gap"
        
username = input("username: ")
password = input("password: ")
print(separator)

if username in users and users[username] == password:       #kontroluje shodu uživatelů a hesel
    print(f"""Welcome to the app, {username}     
We have 3 texts to be analyzed.""")
    print(separator)
    vyber_textu = input("Enter the number btw. 1 and 3 to select: ")    #vstup s výběrem textu k analýze
    print(separator)
    
    if vyber_textu == "1" or vyber_textu == "2" or vyber_textu == "3":  #kontrola žádoucího vstupu
        analyze_text(TEXTS[int(vyber_textu) - 1].split())               #přiřazení konkrétního textu funkci analyze_text dle volby uživatele
    else:
        print("This choice is not allowed.")                            #výpis, pokud vstup není žádoucí
else:
    print(f"unregistered user, terminating the program..")              #hláška při neregistrovaném uživateli


