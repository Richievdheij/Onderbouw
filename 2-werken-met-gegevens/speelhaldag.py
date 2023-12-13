# "Maak een programma speelhaldag.py voor de berekening van de 'Speelhal-dag' van F1.2.02.L1 – van gegevens naar informatie”

print("hoe duur wordt jouw speelhal-dag?")

personen = 4
toegangsticket = 7.45
VIP = 0.37
minuten = 9


total = (toegangsticket * personen + (personen * (minuten * VIP)))
print(total)