# Voorwaarden waar iedereen aan moet voldoen,
# - minimaal 16 jaar
# - sterk genoeg zijn om veel mee terug te nemen, 
# - een positieve instelling hebben, 
# - doorzettingsvermogen hebben en uit het dorp komen tenzij ze in een bos wonen.

investeerder = True
ranger = True
genezer = True
dief = True

print("\n" + "Compleet de vragen om gekwalificeerd te worden als Investeerder, Ranger, Genezer of Dief.")
start = input("Je moet voldoen aan deze minimale kwalificaties, type 'begin' om te starten: ")
if start == "begin":

    startVraag1 = input("Hoe oud ben je?: ")

    if startVraag1 >= ("16"):
        startVraag2 = input("Ben je sterk genoeg om veel mee terug te nemen? Kies 'ja' of 'nee': ")
        if startVraag2 == ("ja"):
            startVraag3 = input("Heb je een positieve instelling? Kies 'ja' of 'nee': ")
            if startVraag3 == ("ja"):
                startVraag4 = input("Heb je doorzettingsvermogen? Kies 'ja' of 'nee': ")
                if startVraag4 == ("ja"):
                    startVraag5 = input("Waar kom je vandaan? Kies 'dorp', 'bos' of 'overig': ")
                    if startVraag5 == ("dorp"):           
                        print("Je bent gekwalificeerd om Investeerder, Ranger, Genezer of Dief te worden! ")         
                    elif startVraag5 == ("bos"):
                        startVraag5bos = print("Je bent gekwalificeerd om Investeerder, Ranger, Genezer of Dief te worden!")
                    else:
                        print("Je bent niet gekwalificeerd als deelnemer.")
                else:
                    print("Je bent niet gekwalificeerd als deelnemer.")
            else:
                print("Je bent niet gekwalificeerd als deelnemer.")
        else:
            print("Je bent niet gekwalificeerd als deelnemer.")
    else:
        print("Je bent niet gekwalificeerd als deelnemer.")