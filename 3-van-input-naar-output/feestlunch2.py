print("Hoeveel croissants wilt u?:")
croissants = input("Aantal croissants: ")

print("Hoeveel broden wilt u?:")
broden = input("Aantal broden: ")

print("Hoeveel kortingsbonnen heeft u?:")
kortingsbon = input("Aantal kortingsbonnen: ")


croissants = int(croissants)
breads = int(broden)
kortingsbon = int(kortingsbon)


crossaintPrice = .39
breadPrice = 2.78
discountPrice = .5

crossaint = croissants * .39
bread = breads * 2.78
discount = kortingsbon * .5

price = croissants + bread
lunchTotal = price - discount

lunchTotal = int(lunchTotal)

print("De feestlunch kost je bij de bakker", lunchTotal, "euro voor de", croissants, "croissantjes en de", breads, "stokbroden als de", kortingsbon, "kortingsbonnen nog geldig zijn!")