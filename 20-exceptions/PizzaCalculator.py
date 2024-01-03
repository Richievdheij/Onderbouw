# Verbeter het programma van de pizzacalculator zodat alle invoer van gehele en breukgetallen is voorzien van exception-handling.

# Richie van der Heij | Opdracht Pizza Calculator
# Maak de Python applicatie "Pizza Calculator" in pizzaCalculator.py in de map van-input-naar-output
# De klant kan een keuze maken uit 3 afmetingen pizza's, namelijk: small, medium en large. Voor elke afmeting wordt er gevraagd hoeveel pizza's de klant wil.

# (OUDE CODE
# print("Hoeveel small pizza's wilt de klant?:")
# pizzasmall = input("Aantal small pizza's: ")

# print("Hoeveel medium pizza's wilt de klant?:")
# pizzamedium = input("Aantal medium pizza's: ")

# print("Hoeveel large pizza's wilt de klant?:")
# pizzalarge = input("Aantal large pizza's: ")


# pizzasmall = int(pizzasmall)
# pizzamedium = int(pizzamedium)
# pizzalarge = int(pizzalarge)

# pizzasmall = pizzasmall * 8.99
# pizzamedium = pizzamedium * 10.49
# pizzalarge = pizzalarge * 12.99

# price = pizzasmall + pizzamedium + pizzalarge
# lunchTotal = price

# lunchTotal = int(lunchTotal)

# print("De pizza's kost je bij de Domino's", lunchTotal, "euro, voor de small pizza", pizzasmall, "euro, voor de medium pizza", pizzamedium, "euro en voor de large pizza", pizzalarge, "euro")

pizzaSmall = 8.99
pizzaMedium = 10.49
pizzaLarge = 12.99
smallAmount = mediumAmount = largeAmount = 0

# Allows the customer to order the 3 different types of pizzas.
def bestellingMaker():
    global smallAmount
    global mediumAmount
    global largeAmount

    pizzaType = input("Wat voor pizza wilt u? Kies uit: 'small', 'medium' of 'large'.").lower()

    while True:
        try:
            inputAmount = int(input("Hoeveel " + str(pizzaType) + " pizza's wilt u? "))
        except ValueError as error:
            print("Dat is geen geldig nummer!")
            continue
        else:
            break

    if pizzaType == "small":
        smallAmount += inputAmount
    elif pizzaType == "medium":
        mediumAmount += inputAmount
    elif pizzaType == "large":
        largeAmount += inputAmount
    else:
        print("Dit is geen type pizza! Vul een geldige type pizza in: 'small', 'medium' of 'large'.")
        bestellingMaker()
    
    meerBestellen()

# Calculates the amount to be paid and passes the receipt to the customer.
def rekeningMaker():
    smallPrice = smallAmount * pizzaSmall
    mediumPrice = mediumAmount * pizzaMedium
    largePrice = largeAmount * pizzaLarge
    totalPrice = smallPrice + mediumPrice + largePrice

    print(" ----------------------------------------------------")
    a = print("|  " + str(smallAmount) + " small pizza's      : " + str(smallPrice) + " euro") if smallAmount > 0 else 0
    b = print("|  " + str(mediumAmount) + " medium pizza's      : " + str(mediumPrice) + " euro") if mediumAmount > 0 else 0
    c = print("|  " + str(largeAmount) + " large pizza's      : " + str(largePrice) + " euro") if largeAmount > 0 else 0
    print("|  Uw totale bedrag is   : " + str(totalPrice) + " euro")
    print(" ----------------------------------------------------")

# Gives the customer the option to continue ordering or to receive the receipt.
def meerBestellen():
    meerVraag = input("Wilt u nog meer bestellen? ").lower()

    if meerVraag == "ja":
        bestellingMaker()
    elif meerVraag == "nee":
        rekeningMaker()
    else:
        print("Dit is geen geldig antwoord. Beantwoord deze vraag alleen met ja of nee.")
        meerBestellen()

bestellingMaker()