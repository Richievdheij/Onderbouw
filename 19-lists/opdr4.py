fruitmand = ['peer', 'ananas', 'appel', 'sinaasappel', 'druif', 'meloen']

def nummer(fruitmand):
    count = 0
    for element in fruitmand:
        count += 1
    return count

print(nummer(fruitmand))