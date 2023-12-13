from asyncore import loop


patat = 0
patatPrijs = 2.50
totaalPatatprijs = 0

mayoSaus = 0.40
aantalMayo = 0
mayoPrijs = 0

frietSaus = 0.25
aantalFrietsaus = 0
frietPrijs = 0

geenSaus = 0
aantalGeen = 0
geenPrijs = 0

frikandel = 0
frikandelPrijs = 2.25
totaalFrikandelprijs = 0

normaalFrikandel = 0
vegaFrikandel = 0
vegaPrijs = 0.25
aantalVegaprijs = 0

metBroodje = 0
prijsBroodje = 1.00
aantalmetbroodje = 0
broodjeZonder = 0

xxlFrikandel = 0
xxlPrijs = 0.50
aantalxxlprijs = 0

kroket = 0
kroketPrijs = 2.00
totaalKroketprijs = 0

totaal = 0
bestelKosten = 1.50

korting = 0


print("Welkom bij Bram Ladage! U kunt 3 gerechten kiezen, patat, frikandel of een kroket\n")

print(
"-| MENU |-",
"KIES UW BESTELLING:",
"\n",
"Patat: €2.50\n",
"Frikandel: €2.00\n",
"Kroket: €2.00\n",
"\n",
)

loop = True
while loop:
    respond = input("")
    if respond == "patat":
        patat = input("Hoeveel patat wilt u? ")

        if float(patat) >= 1:
            for i in range(1, int(patat) + 1):
                saus = input("mayonaise, frietsaus of geen" + "\n")
                if saus == "mayonaise":
                    aantalMayo = aantalMayo + 1
                    mayoPrijs = aantalMayo * mayoSaus
                if saus == "frietsaus":
                    aantalFrietsaus = aantalFrietsaus + 1
                    frietPrijs = aantalFrietsaus * frietSaus
                if saus == "geen":
                    aantalGeen = aantalGeen + 1
                    geenPrijs = aantalGeen * geenSaus

    if respond == "frikandel":
        frikandel = input("Hoeveel frikandellen wilt u? ")

        if float(frikandel) >= 1:
            for i in range(1, int(frikandel) + 1):
                frikandelSoort = input("Normaal, vega(+€0.25) of XXL (+€0,50)")
                if frikandelSoort == "normaal":
                    normaalFrikandel + 1
                
                if frikandelSoort == "vega":
                    vegaFrikandel = vegaFrikandel + 1
                    aantalVegaprijs = vegaPrijs * vegaFrikandel

                if frikandelSoort == "xxl":
                    xxlFrikandel = xxlFrikandel + 1
                    aantalxxlprijs = xxlPrijs * xxlFrikandel    


    if respond == "kroket":
        kroket = input("Hoeveel kroketten wilt u? ")

        if float(kroket) >= 1:
            for i in range(1, int(kroket) + 1):
                broodje = input("Met of zonder broodje? (+€1.00)")
                if broodje == "met":
                    metBroodje = metBroodje + 1
                    aantalmetbroodje = metBroodje * prijsBroodje

                if broodje == "zonder":
                    broodjeZonder = broodjeZonder + 1

    print("Nog meer bestellen? Type 'patat', 'frikandel', of kroket? Anders Type 'Stop'")
    if respond == "stop":
        
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
                "kroketten: " +  str(totaalKroketprijs)
                )

        if totaal >= 1 and totaal <= 9:

            totaal = totaal + bestelKosten

            print(
            "Bestelkosten: " + str(bestelKosten) + "\n"
            )

        if totaal >= 40 and totaal <= 99:

            totaal = totaal / 100 * 95
            korting = totaal / 100 * 95
            korting = totaal - korting

            print(
            "5% korting: " + str(korting)
            )

        if totaal >= 100:

            totaal = totaal / 100 * 92.5
            korting = totaal / 100 * 92.5
            korting = totaal - korting

            print(
            "7.5% korting: " + str(korting)
            )

        if totaal >= 1:
            print("Totaal bedrag: " + str(totaal) + "\n")