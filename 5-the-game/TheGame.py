# FUNCTIONELE EISEN:
# Het spel heeft tenminste 10 acties waar een beslissing moet worden genomen;
# Het restulaat van elke actie dient op het scherm als tekst zichtbaar;
# Het verhaal kent een "win" einde;
# Het verhaal kent meerdere "faal" eindes;
# Het verhaal kent meerdere routes en meerdere eindpunten, je kunt het verhaal dus meerdere keren spelen met verschillende uitkomsten;

# TECHNISCHE EISEN
# Je gebruikt de if else;
# Je gebruikt nested if else;
# Elke if else logt de titel van het level naar de console;
# Je gebruikt alle comparisons en logical operators van w3schools (Dus ook 'groter dan of gelijk aan' etc.)


print("\n" + "Welkom bij het spel 'Richie's dagelijkse schoolleven' \n")

print("!! REMINDER !!")
print("\n" + "Alle antwoorden moeten volledig worden beantwoord. Gebruik van 'CAPS' geeft een fout antwoord.")
startGame = input("Verlos jezelf naar het dagelijkse leven van richie door correcte beslissingen te nemen, onthou de stappen. type 'begin' om verder te gaan. ")
if startGame == "begin":
    
    print(
        "----------------------------------------------------",
        "Het is zondagavond, Richie moet morgen naar school, zijn les begint om 09:00 uur, hij wilt op tijd zijn en minimaal een uur voor zijn les het huis verlaten",
        "Welke bus neemt Richie? Kies uw antwoord.",
        "",
        "A. Richie wordt 07:30 uur wakker, neemt een douche, doet zijn kleding aan, eet als ochtendontbijt een boterham met kaas,",
        "hij verlaat zijn huis om 08:02 uur en vanaf 08:26 uur pakt hij de bus. Met toeval is hij 08:59 uur op school.",
        "",
        "B. Richie wordt telaat wakker, pakt een snel ontbijt, rent om 07:58 uur vanuit zijn huis naar het station",
        "vanuit station is hij net telaat voor zijn bus en pakt de volgende om 08:32 uur. Uiteindelijk is hij 09:02 uur op school.",
        "",
        "C. Richie wordt 07:54 uur wakker, neemt een snelle douche, na het douchen eet hij cornflakes en gaat hij om 07:56 uur richting het station.",
        "Richie arriveert om 08:15 uur op het station, vervolgens pakt hij de bus om 08:26 uur. Tot slot is hij 08:58 uur op school.",
        "----------------------------------------------------",
        sep='\n')

    startVraag1 = input("Wat is correct? Kies 'a', 'b' of 'c': ")

    if startVraag1 == ("c"):

        print(
        "----------------------------------------------------",
        "Richie stapt uit zijn bus bij de rode pijl, hij moet naar gebouw Azzurro, welke route pakt hij? Kies uw antwoord.",
        "",
        "1. Vanuit de rode pijl loopt hij naar Acrobaleno en gaat hij vanuit de binnenkant 1e afslag naar links.",
        "Vervolgens neemt hij een afslag naar rechts.",
        "",
        "2. Vanuit de rode pijl loopt hij naar Da vinci media onderwijsleerbedrijf, vervolgens neemt richie een afslag naar rechts,",
        "loopt langs het samenwerkingsgebouw tot hij bij de eerstvolgende ingang eindigt.",
        "",
        "3. Vanuit de rode pijl neemt hij een afslag naar links, vervolgens bij het laatste gebouw neemt hij een afslag naar rechts.",
        "Daarna pakt hij het eerstvolgende rechts naar een gebouw.",
        "----------------------------------------------------",
        sep='\n')

        startVraag2 = input("Richie is vervolgens op het schoolterrein en moet naar gebouw Azzurro hij kan 3 kanten op, waar moet hij heen? kies '1', '2' of '3'. Kijk naar de tabel en foto 'P. Vraag 2': ")

        if startVraag2 == "2":
            startVraag3 = input("Richie is op school en moet naar Lokaal 2.10, hij kan 2 kanten op, waar moet hij heen? kies 'links' of 'rechts': ")

            if startVraag3 == "links":
                print("U heeft gewonnen, u bent veilig en op tijd bij uw les gearriveerd")
            else: 
                print("U heeft gefaald, helaas!")


        elif startVraag2 == "1":
            startVraag2fout = input("Richie komt aan bij het gebouw Insula College, waar moet hij nu heen? Richting de 'samenwerkingsgebouw' of 'doorlopen' ")

            if startVraag2fout == "samenwerkingsgebouw":
                print("U bent aangekomen, helaas telaat voor de les, u heeft gefaald.")
            else: 
                print("U heeft gefaald, helaas!")

        else:
            print("U eindigt bij het verkeerde gebouw en komt 10 minuten te laat, u heeft gefaald.")

    elif startVraag1 == "a":

        print(
        "----------------------------------------------------",
        "a. Richie gaat eerst naar de les, daarna gaat hij naar de WC. ",
        "",
        "b. Richie gaat eerst naar de WC en vervolgens gaat hij naar zijn les. ",
        "----------------------------------------------------",
        sep='\n')

        startVraag1a = input("Richie is om 08:58 uur op school, hij moet nodig plassen, kies 'a' of 'b'. (kijk tabel) ")

        if startVraag1a == "a":
            print("U voldoet niet aan de minimale eisen, u heeft gefaald.")
        else:
            print("Voldoet niet aan de minimale eisen en komt te laat bij zijn les, u heeft gefaald.")

    else:
        print("Richie is telaat bij zijn les, u heeft gefaald.")





    

    

        
        
