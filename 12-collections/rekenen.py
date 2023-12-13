listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists(list1, list2):
    print("---------\nAdd lists")
    for number in range(len(listOne)):
        print(str(listOne[number]) + " + " + str(listTwo[number]) + " = " + str(listOne[number] + listTwo[number]))

def subtractAndDisplayLists(list1, list2):
    print("---------\nSubtract lists")
    for number in range(len(listOne)):
        print(str(listOne[number]) + " - " + str(listTwo[number]) + " = " + str(listOne[number] - listTwo[number]))

def multiplyAndDisplayLists(list1, list2):
    print("---------\nMultiply lists")
    for number in range(len(listOne)):
        print(str(listOne[number]) + " x " + str(listTwo[number]) + " = " + str(listOne[number] * listTwo[number]))

def devideAndDisplayLists(list1, list2):
    print("---------\nDivide lists")
    for number in range(len(listOne)):
        print(str(listOne[number]) + " / " + str(listTwo[number]) + " = " + str(listOne[number] / listTwo[number]))

addAndDisplayLists(listOne, listTwo)
subtractAndDisplayLists(listOne, listTwo)
multiplyAndDisplayLists(listOne, listTwo)
devideAndDisplayLists(listOne, listTwo)