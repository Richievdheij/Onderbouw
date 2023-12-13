total = 0

# Aantal prijs in goud
diamant = 270
kroon = 93
robijn = 6.75
ring = 46.5
armband = 26.63

# Hoeveel items in goud
# diamant = 1
# kroon = 1
# robijn = 3
# ring = 6
# armband = 8

vraag1 = 3 * 5
vraag2 = (11 * 44) / 10
vraag3 = (2 * 15) / 5 / 10

# Munten
# 5x zoveel goud als het antwoord op de eerste vraag van de troll: 15 goud
# 11x zoveel zilver als het antwoord op de tweede vraag van de troll: 484 zilver - 48.4 goud
# 15x zoveel koper als het antwoord op de derde vraag van de troll: 30 koper - 0.6 goud

start = print("\n" + "Reken uit het totale waarde")

totaalPrijs = diamant + kroon + robijn + ring + armband
print("Totale prijs items", totaalPrijs, "goud")

total = totaalPrijs + vraag1 + vraag2 + vraag3
print("Het totale prijs met munten is", total, "goud")
