items = {
    "bolletje": {
        "price": 0.95,
        "amount": 0,
    },

    "liter": {
        "price": 9.8,
        "amount": 0
    },

    "hoorntje": {
        "price": 1.25,
        "amount": 0,
    },

    "bakje": {
        "price":  0.75,
        "amount": 0,
    },
}

# Topping amounts / prices
toppings = {    
    "geen": {
        "price": 0,
        "amount": 0
    },

    "slagroom": {
        "price":0.5,
        "amount": 0,
    },
    
    "sprinkels": {
        "price":0.3,
        "amount": 0,
    },

    "caramel_saus": {
        "hoorntje": {
            "price": 0.6,
            "amount": 0
        },

        "bakje": {
            "price": 0.9,
            "amount": 0
        },
    
        "amount": 0,
    }
}

print("Welkom bij Papi Gelato")

hoeveelBolletjes = 0
bolletjeHoorntje = 0
topping = 0

def bolletjes():
    global hoeveelBolletjes
    global bolletjeHoorntje
    askQuestion = True
    while askQuestion:
        hoeveelBolletjes = input("Hoeveel bolletjes wilt u? ")
        if hoeveelBolletjes.isdigit():
            hoeveelBolletjes = int(hoeveelBolletjes)
            smaken()

            if hoeveelBolletjes >= 4 and hoeveelBolletjes <= 8:
                print(f"Dan krijgt u van mij een bakje met {hoeveelBolletjes} bolletjes")
                bolletjeHoorntje = "bakje"
                stap3(bolletjeHoorntje, hoeveelBolletjes)
                
            elif hoeveelBolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet")

            if hoeveelBolletjes >= 1 and hoeveelBolletjes <= 8:
                askQuestion = False

        else:
            print("Sorry dat snap ik niet...")

    return hoeveelBolletjes

def stap2(aantalBolletjes):
    global bolletjeHoorntje
    askQuestion = True
    while askQuestion:
        bolletjeHoorntje = input(f"Wilt u deze {aantalBolletjes} bolletje(s) in A) een hoorntje of B) een bakje? ").lower()
        if bolletjeHoorntje == "a" or bolletjeHoorntje == "b":
            bolletjeHoorntje = "bakje" if bolletjeHoorntje == "b" else "hoorntje"
            tops()
            askQuestion = False

        else:
            print("Sorry, dat snap ik niet...")

def stap3(bolletjeHoorntje, aantalBolletjes):
    add_items()
    askQuestion = True
    while askQuestion:
        totaalBolletjes = input(f"Hier is uw {bolletjeHoorntje} met {aantalBolletjes} bolletje(s). Wilt u nog meer bestellen? (Y/N) ").lower()
        if totaalBolletjes == "y":
            askQuestion = False
            main()
            
        elif totaalBolletjes == "n":
            print("Bedankt en tot ziens!")
            askQuestion = False
            receipt()
            
        else:
            print("Sorry, dat snap ik niet...")

def smaken():
    for x in range(1, hoeveelBolletjes+1):
        askQuestion = True
        while askQuestion:
            bolletjeSmaak = input(f"Welke smaak wilt u voor bolletje nummer {x}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ").upper()
            if bolletjeSmaak == "A" or bolletjeSmaak == "C" or bolletjeSmaak == "M" or bolletjeSmaak == "V":
                print("")
                askQuestion = False
        
            else:
                print("Sorry dat snap ik niet...")

def tops():
    global topping
    smaak = ("geen", "slagroom", "sprinkels", "caramel saus")
    choice = ("a", "b", "c", "d")
    askQuestion = True
    while askQuestion:
        input_answer = input(f"Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ").upper()
        if input_answer in choice:
               
            index = choice.index(input_answer)
            topping = smaak[index].replace(" ", "_")
            askQuestion = False
            
        else:
            print("Sorry dat snap ik niet...")

def add_items():
    items['bolletje']['amount'] += int(hoeveelBolletjes)
    items[bolletjeHoorntje]['amount'] += 1

    try:
        if isinstance(toppings[topping]['amount'], int):
            toppings[topping]['amount'] += 1
        else:
            toppings[topping]['amount'][bolletjeHoorntje] += 1
    except KeyError:
        pass
    finally:
        if isinstance(toppings[topping]['amount'], int):
            toppings[topping]['amount'] += 1

def receipt():
    total_receipt_price = 0
    print('---------["Papi Gelato"---------')
    for item, info in items.items():
        if info['amount'] > 0:
            total_price = info['amount'] * info['price']
            total_receipt_price += total_price

            print(f"{item}      {info['amount']} * €{info['price']} =   €{round(total_price, 2)}")
    print("                         -------- +")
    print(f"Totaal                       €{total_receipt_price}")

def main():
    aantalBolletjes = bolletjes()

    if aantalBolletjes >= 1 and aantalBolletjes <= 3:
        stap2(aantalBolletjes)

if __name__ == "__main__":
    main()
