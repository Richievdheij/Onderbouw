# Herhaal een input() tot het resultaat daarvan gelijk is aan ‘quit’. Print het aantal iteraties per iteratie. (Het aantal keren dat de vraag is gesteld)

not_right = 0

while input("Type 'quit': ") != "quit":
    not_right += 1
    print(not_right)
else:
    not_right += 1
    print(not_right)