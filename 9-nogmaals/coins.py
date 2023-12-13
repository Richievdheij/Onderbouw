# name of student: Richie van der Heij
# number of student: 99058860
# purpose of program: Print a answer to the user how he can pay the total price with the fastest method
# function of program: Calculate how the user can pay the price 
# structure of program: Loop through the program if the user has not paid the total price

receipt = []

toPay = int(float(input('Amount to pay: ')) * 100) # Ask how many the user already paid, and change it into a number
paid = int(float(input('How many have you paid: ')) * 100) # Ask how much the total price is, and change it into a number

change = paid - toPay # Calculate the change the user must pay

if change > 000: # Check if the user must pay more
  coinValue = 500 # The amount of cents the user must pay
  
# Change the coin value to "euro" or "cents"

  while change > 0 and coinValue > 0: 
    nrCoins = change // coinValue # Calculate how many coins the user must give back with the coinValue amount

    # Change the coin value to "euro" or "cents"

    if coinValue >= 100:
      coinValue_name = "euro"
      coinValue_str = str( coinValue // 100 ) # Change the value of the coin the user must pay, to a string

    else:
      coinValue_name = " cents"
      coinValue_str = str(coinValue) # Change the value of the coin the user must pay, to a string


    if nrCoins > 0: # Number of coins the user must pay
      print(f"return maximal {nrCoins} coins of {coinValue_str} {coinValue_name}") # Print the amount of coins the user must give back with the specific amount

      nrCoinsReturned = input(f"How many coins of {coinValue_str} {coinValue_name} did you return? ") # Ask the user how many coins he has paid with the specific value
      change -= int(nrCoinsReturned) * coinValue # The change gets decreased with the value the user has paid\

      # If the coins the user has given back is higher than 0
      if nrCoinsReturned:

        receipt_info = f"{nrCoinsReturned} coin(s) of {coinValue_str} {coinValue_name} has been given back"
        receipt.append(receipt_info)

# comment on code below: 
  
coinArray = [500, 300, 200, 50, 20, 10, 5, 2, 1, 0] # Array with all the coin values

coinValue_position = ( coinArray.index(coinValue) + 1 ) # Get the position of the coin the user did answer + 1

coinValue = coinArray[coinValue_position] # Change the coin value with the coinValue_positions variable

# If the user has not paid everything
if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
# If the user paid everything
else:
  print('done')

# Print every coin with the amount the user has given back
  for info in receipt:
      print(info)



