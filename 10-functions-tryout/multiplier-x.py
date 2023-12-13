number = False

while not number:
    user_number = input("Van welk getal wilt u de tafel zien?: ")

    try:
        user_number = int(user_number)
    except:
        print("Vul een geldig nummer in")
    else: 
        if user_number <= 0:
            print("Vul een getal hoger dan 0 in")
        else:   
            number = True

def makeTable(number):
    for i in range(1, 11):
        answer = number * i

        userNumber_str = str(number)
        num_str = str(i)
        answer = str(answer)

        string = userNumber_str + " * " + num_str + " = " + answer
        
        print(string)


makeTable(user_number)

# OF

antwoord = input("Van welk nummer wilt u de tafel hebben? ")

def tafelVan(nummer):
    for x in range(1, 11):
        print(str(x) + " * " + nummer + " = " + str(x * int(nummer)))

tafelVan(antwoord)