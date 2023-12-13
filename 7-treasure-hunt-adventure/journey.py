# Opdracht 2
# de schatting van de prijs van de gehele reis (heen- en terug). Hoeveel het gaat kosten wordt in goud (met 2 cijfers achter de komma) getoond.

# Wat de groep wilt kopen: (heenweg, 6 personen)
# - 3x paarden huren (per dag, silver)
# - 2x 3 persoonstent (goud)
# - 6x 3 dagen in een Inn (per dag) (zilver & koper)
# - 6x 5 dagen eten (per dag, koper)

# Omzetten goud

koper = 0.02
zilver = 0.1
goud = 1
platinum = 24

# Bedragen in goud

paardenHuur = 12
persoonsTent = 16
slapenInn = 6
slapenInnPaard = 1.62
eten = 3.5

totaleBedrag = (paardenHuur + (persoonsTent + (slapenInn + (slapenInnPaard + (eten)))))
totaal = totaleBedrag * 2

print("----------------------------------------------------")
print("Totale bedrag heenreis in goud met 5 personen")
print(totaleBedrag)
print("")
print("Totale bedrag per persoon")
print("7.11 goud")
print("Totale bedrag heen en terugreis in goud")
print(totaal)
print("----------------------------------------------------")