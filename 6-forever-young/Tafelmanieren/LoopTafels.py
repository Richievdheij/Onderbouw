# Print de tafel van een op te geven getal met input() Bijv. 1 x 4 = 4 ; 2 x 4 = 8 etc t/m 10 x 4 = 40

tafel = input("Welke tafel wilt u? ")
hoeveelheid = input("Tot welk cijfer moet die tafel gaan? ")

for x in range(1, int(hoeveelheid) + 1):
    print(tafel + " * " + str(x) + " = " + str(int(tafel) * x))
