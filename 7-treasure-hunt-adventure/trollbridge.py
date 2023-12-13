#Beantwoord de 3 dagen voor gratis toegang.
# 1. Het gemiddelde van 3 getallen is 21. Een getal is 15, de andere 2 zijn het zelfde, wat getal is dat?

3

# 2. Als 2 kip 8 eieren leggen in 3 dagen. Hoeveel eieren leggen 3 kippen in een week?

44

# 3. Hoe vaak komt het cijfer 6 voor tussen 7 en 111?

2

for x in range(7, 111, 6):
    print(x)

import time
start = input("\n" + "Je ontmoet een troll die de brug blokkeert, hij vraagt jou om 3 raadsels op te lossen, type 'begin' om te starten: ")
if start == "begin":
    startVraag1 = input("Het gemiddelde van 3 getallen is 21. Een getal is 15, de andere 2 zijn het zelfde, wat getal is dat?: ")
    time.sleep(1) 
    if startVraag1 == "3":
        startVraag2 = input("Als 2 kip 8 eieren leggen in 3 dagen. Hoeveel eieren leggen 3 kippen in een week?: ")
        time.sleep(1) 
        if startVraag2 == "44":
            startVraag3 = input("Hoe vaak komt het cijfer 6 voor tussen 7 en 111?: ")
            time.sleep(1) 
            if startVraag3 == "2":
                print("Je mag gratis de brug over!")
            else:
                print("Je mag de brug niet over, betaal 55 goud")
        else:
            print("Je mag de brug niet over, betaal 55 goud")
    else:
        print("Je mag de brug niet over, betaal 55 goud")
else:
    print("Je mag de brug niet over, betaal 55 goud")