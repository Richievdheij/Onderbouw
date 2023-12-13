def addition(number1, number2):
    
    answer = number1 + number2
    
    number1 = str(number1)
    number2 = str(number2)
    answer = str(answer)

    string = number1 + " + " + number2 + " = " + answer
    print(string)


def subtraction(number1, number2):
    
    answer = number1 - number2
    
    number1 = str(number1)
    number2 = str(number2)
    answer = str(answer)

    string = number1 + " - " + number2 + " = " + answer
    print(string)


def multiplication(number1, number2):
    answer = number1 * number2

    number1 = str(number1)
    number2 = str(number2)
    answer = str(answer)
    
    string = number1 + " * " + number2 + " = " + answer
    print(string)


def division(number1, number2):
    
    answer = number1 / number2

    number1 = str(number1)
    number2 = str(number2)
    answer = str( int(answer) )
    

    string = number1 + " / " + number2 + " = " + answer
    print(string)


def increment(number):
    
    answer = number + 1

    number = str(number)
    answer = str(answer)

    string = number + " + 1 = " + answer
    print(string)


def decrement(number):
    
    answer = number - 1

    number = str(number)
    answer = str(answer)

    string = number + " - 1 = " + answer
    print(string)


addition(10, 12)
subtraction(58, 34)
multiplication(6, 7)
division(144, 12)
increment(12)
decrement(34)