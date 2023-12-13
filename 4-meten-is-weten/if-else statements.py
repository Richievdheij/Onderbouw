print("\n" + "Als u niks invult, of niet 'ja' of 'nee', wordt het antwoord automatisch 'nee' \n")

cheese_yellow = input("Is de kaas geel?: ")

if cheese_yellow == "ja":
    cheese_gaps = input("zitten er gaten in?: ")

    if cheese_gaps == "ja":
        overpriced = input("Is de kaas belachelijk duur?: ")

        if overpriced == "ja":
            print("Emmenthaler")
        else: 
            print("Leerdammer")

    else:
        cheese_stone = input("Is de kaas hard als steen?: ")

        if cheese_stone == "ja":
            print("Pammigiano Reggiano")
        else: 
            print("Goudse kaas")



else:
    blue_mold = input("Heeft de kaas blauwe schimmels: ")

    if blue_mold == "ja":
        cheese_crust_mold = input("Heeft de kaas een korst?: ")

        if cheese_crust_mold == "ja":
            print("Bleu de Rochbaron")
        else:
            print("Foumme d'Ambert")
    
    else:
        cheese_crust_not_mold = input("Heeft de kaas een korst?: ")

        if cheese_crust_not_mold == "ja":
            print("Camembert")
        else: 
            print("Mozzarella")