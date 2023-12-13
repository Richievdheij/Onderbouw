# Het programma kan het volgende:

# Je kunt herhaald getallen raden
# Het spel stopt na 20 te raden getallen of als je aangeeft (eerder) te willen stoppen. Elke te raden getal heet een ronde. Het spel heeft dus maximaal 20 ronden.
# Het programma neemt een random geheim te raden getal in gedachten tussen de 1 en de 1000
# Je mag 10 keer raden. Is het dan nog niet geraden, dan stopt die ronde.
# Voor elk geraden getal wordt de score opgehoogd met 1. Je kunt dus maximaal 20 punten scoren.
# Na elke gok geeft het programma antwoord: geraden, of hoger of lager
# Als het (absolute) verschil tussen het getal dat jij gokt en het geheime te raden getal kleiner is dan 50 dan meldt het programma in de terminal: 'Je bent warm’
# Als het (absolute) verschil tussen het getal dat jij gokt en het geheime te raden getal kleiner is dan 20 dan meldt het programma in de terminal: 'Je bent heel warm’
# Na elke ronde meldt het programma de score tot dan toe in de terminal
# Na elke ronde vraagt het programma: ‘Nog een getal raden?’ tenzij er al 20 ronden zijn geweest.
# Aan het einde meldt het programma de eindscore.

import random

x = 1
randomNum = 0
score = 0
aantalGeraden = 0

while x < 21:
    y = 0
    randomNum = random.randint(1, 1000)
    print("ronde", x)
    while y < 10:
        antwoord = int(input("voer een getal in tussen 1 en 1000: "))
        if antwoord == randomNum:
            y = 10
            score += 1
            print("U heeft het antwoord geraden!")
        elif antwoord - randomNum <= 20 and antwoord - randomNum > 0 or randomNum - antwoord <= 20 and randomNum - antwoord > 0:
            print("U bent heel warm")
        elif antwoord - randomNum <= 50 and antwoord - randomNum > 0 or randomNum - antwoord <= 50 and randomNum - antwoord > 0:
            print("U bent warm")
        elif antwoord > randomNum:
            print("U moet lager raden")
        else:
            print("U moet hoger raden")
        y += 1
        aantalGeraden += 1
    if x < 20:
        antwoord = input("Wilt u stoppen met spelen? ")
        if antwoord.lower() == "ja":
            x = 20
        
    x += 1

print("-----------------------------")
print("U heeft " + str(aantalGeraden) + " keer geraden")
print("U heeft " + str(score) + " keer goed geraden!")
print("-----------------------------")