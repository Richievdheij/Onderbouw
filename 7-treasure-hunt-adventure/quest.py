# Aangepaste bedrag met 1 overnachting meer in de tent (heen en terugreis)

# Omzetten goud

koper = 0.02
zilver = 0.1
goud = 1
platinum = 24

# Bedragen in goud

paardenHuur = 12
persoonsTent = 16
slapenInn = 4
slapenInnPaard = 1.08
eten = 3.5

totaleBedrag = (paardenHuur + (persoonsTent + (slapenInn + (slapenInnPaard + (eten)))))
totaal = totaleBedrag * 2

# Hoeveel stuks:
# schep = 4
# klimuitrusting = 0
# lantaren = 2
# lampenolie = 3
# hengel = 2
# tinderbox = 3
# rugzak = 5
# touw = 24
# muggennet = 0
# fakkel = 5
# waterzak = 6

# Prijs boodschappenlijst in goud

schep = 2
klimuitrusting = 14
lantaren = 4
lampenolie = 0.22
hengel = 2
tinderbox = 0.4
rugzak = 3
touw = 0.14
muggennet = 0.12
fakkel = 0.06
waterzak = 4

boodschappenlijst = schep + lantaren + lampenolie + hengel + tinderbox + rugzak + touw + fakkel + waterzak

total = 0
eindbedrag = 0

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
troll = 55
eindbedrag2 = 65.26

# Munten
# 5x zoveel goud als het antwoord op de eerste vraag van de troll: 15 goud
# 11x zoveel zilver als het antwoord op de tweede vraag van de troll: 484 zilver - 48.4 goud
# 15x zoveel koper als het antwoord op de derde vraag van de troll: 30 koper - 0.6 goud

totaalPrijs = diamant + kroon + robijn + ring + armband
print("Totale prijs items", totaalPrijs, "goud")

total = totaalPrijs + vraag1 + vraag2 + vraag3
print("Het totale prijs met munten is", total, "goud")

totalkosten = totaleBedrag + totaal + boodschappenlijst
print("Totale kosten en bedrag in goud is", totalkosten, "goud")

verdelen = total - diamant
print("Gestolen diamant die gestolen was is", verdelen, "goud")

eindbedrag = total - totalkosten - troll
print(eindbedrag, "heeft het reisje opgebracht (exclusief verdeling)")

eindbedrag2 = eindbedrag / 5

print("----------------------------------------------------")
print("Totale bedrag heenreis in goud met 5 personen")
print(totaleBedrag)
print("")
print("Totale bedrag heen- & terugreis in goud")
print(totaal)
print("")
print("Totale bedrag boodschappenlijst in goud")
print(boodschappenlijst)
print("")
print("Totale bedrag treasure in goud")
print(total)
print("")
print("Totale kosten en bedrag in goud")
print(totalkosten)
print("")
print("Totale eindbedrag")
print(eindbedrag)
print("")
print("Totaal opgeleverd per persoon")
print(eindbedrag2)
print("----------------------------------------------------")