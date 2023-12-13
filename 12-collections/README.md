## collections

# Dagen:
Maak een List aan waarin de dagen van de week zitten: maandag t/m zondag. De volgende uitvoer laat je in de terminal zien waarbij je gebruik moet maken van het 'aanspreken' van de list met de dagen die je hebt aangemaakt. Gebruik een for-loop waar mogelijk.

- Alle dagen van de week zijn: maandag, dinsdag, woensdag, donderdag, vrijdag, zaterdag, zondag.
- De werkdagen zijn: maandag, dinsdag, woensdag, donderdag, vrijdag.
De weekenddagen zijn: zaterdag, zondag.
- Alle dagen van de week in omgekeerde volgorde zijn: zondag, zaterdag, vrijdag, donderdag, woensdag, dinsdag, maandag.
- De werkdagen in omgekeerde volgorde zijn: vrijdag, donderdag, woensdag, dinsdag, maandag.
- De weekenddagen in omgekeerde volgorde zijn: zondag, zaterdag.

# listOne:
- listOne met daarin de getallen: 1,2,3,4,5,6,7,8,9,10

# listTwo:
- listTwo met daarin de getallen: 2,4,6,8,10,12,14,16,18,20

In je oplossing maak je vier functies (def) aan die de berekeningen uitvoeren en de uitvoer naar het scherm schrijven:
addAndDisplayLists (list1, list2):

Add lists
1 + 2 = 3
2 + 4 = 6
3 + 6 = 9
4 + 8 = 12
5 + 10 = 15
6 + 12 = 18
7 + 14 = 21
8 + 16 = 24
9 + 18 = 27
10 + 20 = 30

substractAndDisplayLists (list1, list2):

Multiply lists
  1 *  2 = 2        
  2 *  4 = 8
  3 *  6 = 18
  4 *  8 = 32
  5 * 10 = 50
  6 * 12 = 72
  7 * 14 = 98
  8 * 16 = 128
  9 * 18 = 162
 10 * 20 = 200

 divideAndDisplayLists (list1, list2):

 Divide lists
 1 /  2 = 0.5
 2 /  4 = 0.5
 3 /  6 = e.5
 4 /  8 = 0.5
 5 / 10 = 0.5
 6 / 12 = 0.5
 7 / 14 = 0.5
 8 / 16 = 0.5
 9 / 18 = 0.5
10 / 20 = 0.5

Let op: de getallen in de uitvoer moeten worden uitgelijnd

# Spelprogramma:
- Maak een list spelList van de volgende spellen: 'Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet' en 'Cluedo'

- Maak nu een function def spelProgramma(spelList) die een list teruggeeft met een willekeurig aantal (minimaal 3 en maximaal 10) te spelen spelletjes willekeurig gekozen uit de spelList. Er mogen dubbele spelletjes in de teruggegeven list zitten.
- Breid nu de function uit tot def spelProgramma(spelList, minimum) waarvoor geldt dat mimimum het minimaal aantal spellen is dat de teruggegeven list bevat.
- Breid nu de function uit tot def spelProgramma(spelList, minimum, maximum) waarvoor geldt dat maximum het maximaal aantal spellen is dat de teruggegeven list bevat.