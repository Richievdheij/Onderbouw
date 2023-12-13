output = ""

def functie():
    naam = input("Vul hier een naam in: ")
    if naam.lower() == "stop":
        return "stop"
    leeftijd = input("Vul hier een leeftijd in: ")
    if leeftijd.lower() == "stop":
        return "stop"
    return "Hallo " + naam + ". Uw leeftijd is " + leeftijd + " jaar."

while output != "stop":
    output = functie()
    if output != "stop":
        print(output)