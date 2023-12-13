# Richie van der Heij | Opdracht Pizza Calculator
# Maak de Python applicatie "Pizza Calculator" in pizzaCalculator.py in de map van-input-naar-output
# De klant kan een keuze maken uit 3 afmetingen pizza's, namelijk: small, medium en large. Voor elke afmeting wordt er gevraagd hoeveel pizza's de klant wil.

print("Hoeveel small pizza's wilt de klant?:")
pizzasmall = input("Aantal small pizza's: ")

print("Hoeveel medium pizza's wilt de klant?:")
pizzamedium = input("Aantal medium pizza's: ")

print("Hoeveel large pizza's wilt de klant?:")
pizzalarge = input("Aantal large pizza's: ")


pizzasmall = int(pizzasmall)
pizzamedium = int(pizzamedium)
pizzalarge = int(pizzalarge)

pizzasmall = pizzasmall * 8.99
pizzamedium = pizzamedium * 10.49
pizzalarge = pizzalarge * 12.99

price = pizzasmall + pizzamedium + pizzalarge
lunchTotal = price

lunchTotal = int(lunchTotal)

print("De pizza's kost je bij de Domino's", lunchTotal, "euro, voor de small pizza", pizzasmall, "euro, voor de medium pizza", pizzamedium, "euro en voor de large pizza", pizzalarge, "euro")