patat = 0
patatPrijs = 2.50
totaalPatatprijs = 0
totaalPatat = 0

frikandel = 0
frikandelPrijs = 2.00
totaalFrikandelprijs = 0

kroket = 0
kroketPrijs = 2.00
totaalKroketprijs = 0

totaal = 0
bestelKosten = 1.50

korting = 0

print("Welkom bij Bram Ladage! U kunt 3 gerechten kiezen, patat, frikandel of een kroket\n")

patat = input("Hoeveel patat wilt u? ")
frikandel = input("Hoeveel frikandellen wilt u? ")
kroket = input("Hoeveel kroketten wilt u? ")

print("\n")

totaalPatat = patat
totaalPatatprijs = float(patat) * patatPrijs
totaalFrikandelprijs = float(frikandel) * frikandelPrijs
totaalKroketprijs = float(kroket) * kroketPrijs

totaal = totaalFrikandelprijs + totaalPatatprijs + totaalKroketprijs

if totaal == 0:
    print("U heeft geen bestelling")

if totaal >= 1:
    print(
    "RECEIPT BESTELLING\n"
    )
    if float(patat) >= 1:
        print(
        "Patat: " + str(totaalPatatprijs)
        )

    if float(frikandel) >= 1:
        print(
        "Frikandellen: " + str(totaalFrikandelprijs)
        )

    if float(kroket) >= 1:
        print(
        "Kroketten: " +  str(totaalKroketprijs)
        )

if totaal >= 1 and totaal <= 9:

    totaal = totaal + totaalKroketprijs

    print(
    "Bestelkosten: " + str(totaalKroketprijs
) + "\n",
    )
    
if totaal >= 40 and totaal <= 99:

    totaal = totaal / 100 * 95
    korting = totaal / 100 * 95
    korting = totaal - korting

    print(
        "5% korting: " + str(korting),
        )

if totaal >= 100:

    totaal = totaal / 100 * 92.5
    korting = totaal / 100 * 92.5
    korting = totaal - korting

    print(
        "7.5% korting: " + str(korting),
        )

if totaal >= 1:
    print("Totaal bedrag: " + str(totaal) + "\n",)