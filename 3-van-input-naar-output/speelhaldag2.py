print("Hoeveel personen gaan er mee?:")
persons = input("Aantal personen: ")

print("Hoelang VR minuten wilt u? (stappen van 5 minuten):")
gameseat_Minutes = input("Aantal VR minuten: ")

persons = int(persons)
gameseat_Minutes = int(gameseat_Minutes)



ticketTotal = persons * 7.45 

gameseat_price = (gameseat_Minutes / 5) * .37
gameseatTotal = gameseat_Minutes * persons

arcadeTotal = gameseatTotal + ticketTotal

arcadeTotal = int(arcadeTotal)

print("Dit geweldige dagje-uit met", persons, "mensen in de Speelhal met", gameseat_Minutes, "minuten VR kost je maar", arcadeTotal, "euro")