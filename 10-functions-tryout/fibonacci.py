# example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765


def fibonacci(totalLoop):

    # Variables for the numbers
    num1 = 0
    num2 = 1

    endNumbers = [] # Array for the last 2 numbers


    # Loop through the fibonacci numbers
    for x in range(1, totalLoop):  

        # Add the last 2 numbers to the array 
        if x >= (totalLoop - 2):
            endNumbers.append(num1) # Add the number to the endNumbers array

        print(num1) # Print the number

        # Calculate the values for the next number
        totalNum = num1 + num2
        
        num1 = num2
        num2 = totalNum


    else:
        return endNumbers # Return the number array


numbers = fibonacci(22) # Run the function


ratio = numbers[0] / numbers[1] # Calculate the ratio

print(ratio)