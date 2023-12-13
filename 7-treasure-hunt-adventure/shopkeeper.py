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

print("----------------------------------------------------")
print("Totale bedrag heenreis in goud met 5 personen")
print(totaleBedrag)
print("")
print("Totale bedrag per persoon in goud")
print("7.11")
print("")
print("Totale bedrag heen- & terugreis in goud")
print(totaal)
print("")
print("Totale bedrag boodschappenlijst in goud")
print(boodschappenlijst)
print("----------------------------------------------------")

start = input("\n" + "Geef de minimale hoeveelheid producten die je wilt hebben, type 'begin' om te starten: ")
if start == "begin":
    print("Hoeveel scheppen wilt de klant?:")
    schep = input("Aantal scheppen: ")

    print("Hoeveel klimuitrusting wilt de klant?:")
    klimuitrusting = input("Aantal klimuitrusting: ")

    print("Hoeveel lamtaren wilt de klant?:")
    lantaren = input("Aantal lantaren: ")

    print("Hoeveel lampenolie's wilt de klant?:")
    lampenolie = input("Aantal lampenolie: ")

    print("Hoeveel hengels wilt de klant?:")
    hengel = input("Aantal hengels: ")

    print("Hoeveel tinderboxen wilt de klant?:")
    tinderbox = input("Aantal tinderboxen: ")

    print("Hoeveel rugzakken wilt de klant?:")
    rugzak = input("Aantal rugzakken: ")

    print("Hoeveel touw wilt de klant?:")
    touw = input("Aantal touw: ")

    print("Hoeveel muggennetten wilt de klant?:")
    muggennet = input("Aantal muggennetten: ")

    print("Hoeveel fakkels wilt de klant?:")
    fakkel = input("Aantal fakkels: ")

    print("Hoeveel waterzakken wilt de klant?:")
    waterzak = input("Aantal waterzakken: ")

    print("Totale producten kosten in totaal", boodschappenlijst, "goud")