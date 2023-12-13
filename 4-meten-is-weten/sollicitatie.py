print("\n" + "Geef correct antwoord op de vragen voor een sollicitatietest! Beantwoord met 'ja' en 'nee' of met cijfers. \n")

# Hoeveelheid jaren ervaring
ervaring_dressuur = 4
ervaring_jongleren = 5
ervaring_acrobatiek = 3

# Correcte antwoorden
hasDiploma = "ja"
hasLicense = "ja"
hasHat = "ja"
hasManWoman = "ja"
hasLength = "150"
hasWeight = "90"
hasCertificaat = "ja"
hasShoes = "ja"
hasShirt = "ja"
hasSpeed = "ja"
hasPants = "ja"

ervaring_dressuur = input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? ")


if ervaring_dressuur >= "4":
    ervaring_jongleren = input("Hoeveel jaar praktijkervaring heeft u met jongleren? ")

    if ervaring_jongleren >= "5":
        ervaring_acrobatiek = input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? ")

        if ervaring_acrobatiek >= "3":
            hasDiploma = input("Bent u in bezit van een MBO-4 diploma ondernemen? ")

    if hasDiploma == "ja":
        haslicense = input("Bent u in bezit van een geldig vrachtwagen rijbewijs? ")
        
if hasLicense == "ja":
    hasHat = input("Bent u in bezit van een hoge hoed? ") 
        
    if hasHat == "ja":
        hasLength = input("Wat is uw lengte? ")

        if hasLength >= "150":
            hasWeight = input("Wat is uw lichaamsgewicht? ")

    if hasWeight >= "90":
        hasCertificaat = input("Bent u in bezit van een certificaat? ")
    
if hasCertificaat == "ja":
    hasManWoman = input("Bent u een man of een vrouw? Kies 'ja' voor man, 'nee' voor vrouw. ")
    
    if hasManWoman == "ja":
        input("Wat is uw snorbreedte? ")
    else: 
        input("Wat is uw krulhaarlengte? ")
    
# 4 extra vragen
        hasShoes == input("Bent u in bezit van dichte schoenen? ")

    if hasShoes == "ja":
        hasShirt = input("Bent u in bezit van shirts met lange mouwen?")

        if hasShirt == "ja":
            hasSpeed = input("Bent u snel handelend? ")

    if hasSpeed == "ja":
        hasPants = input("Bent u in bezit van een lange cargobroek? ")

print("Gefeliciteerd! U bent uitgenodigd voor een sollicitatie.")

   

