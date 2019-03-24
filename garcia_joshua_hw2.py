# Name: Josh Garcia
# Section: C
# Project: Snack Machine
# Description: To create a Finite State Machine that represents a snack machine.

# Initiating initial values for varibles
state = 'A'
snack_1 = ['Doritos', 2, 2.50]
snack_2 = ['Donuts', 4, 2.50]
snack_3 = ['Pretzels', 1, 2.50]
total = 0

# Creating a while loop that can only be broken when state = G
while True:
    if state == 'A':
        i = input("Type 'start' to start:\nType 'exit' to exit:\n\n")
        
        if i == 'start': 
            state = 'B'

        if i == 'exit':
            state = 'G'

        # If snack inventory is zero, move to state = F, to restock snack
        if snack_1[1] == 0 or snack_2[1] == 0 or snack_3[1] == 0:
            state = 'F'

    # state = B displays snacks with price, initiate coin insert
    if state == 'B':
        print("\n>>> DISPLAY <<<")
        print("\n{} at ${:.2f}\n{} at ${:.2f}\n{} at ${:.2f}\n".format(snack_1[0], snack_1[2], snack_2[0], snack_2[2], snack_3[0], snack_3[2]))
        
        coin = float(input("Please insert coin: "))
        total = coin

        if coin >= 2.50:
            print("${:.2f} inserted\n".format(coin))
            state = 'C'

        # If first coin does not cover cost, move to this while loop to collect the rest of coins
        while total < 2.50:
            coin = float(input("Please insert another coin: "))
            total += coin
            
            # If total amount of coins >= than the price, break out of the while and move to state = C
            if total >= 2.50:
                print("${:.2f} inserted".format(total))
                state = 'C'
                break

    # this state will let you select what snack you want
    if state == 'C':
        snack_selection = input("Please select snack. \n--------\n{}\n{}\n{}\n--------\nrefund\n\n".format(snack_1[0], snack_2[0], snack_3[0]))

        if snack_selection == 'Doritos':
            # if inventory is out, let user know snack is out and to select different snack
            if snack_1[1] == 0:
                print('\nWe are all out, please select another snack.')
                state = 'C'
            else:
                snack_1[1] -= 1
                state = 'D'

        if snack_selection == 'Donuts':
            if snack_2[1] == 0:
                print('\nWe are all out, please select another snack.')
                state = 'C'
            else:
                snack_2[1] -= 1
                state = 'D'

        if snack_selection == 'Pretzels':
            if snack_3[1] == 0:
                print('\nWe are all out, please select another snack.')
                state = 'C'
            else:
                snack_3[1] -= 1
                state = 'D'
        
        # If refund is selected, move to state = E, to return money
        if snack_selection == 'refund':
            total = total - total
            print('\nMoney has been refunded. \n')
            state = 'A'

    # state = D will Dispense snack, move onto state = E
    if state == 'D':
        print('\nDispensing Snack...\n')
        change = total - 2.50
        state = 'E'

    # state E will return any change back to the user
    if state == 'E':

        if change >= 0:
            print('Returning Change of ${:.2f}\n'.format(change))
            state = 'A'

    # If the inventory is empty, restock the vending machine
    if state == 'F':
        print('\nRestocking vending machine...')
        state = 'A'

        # This while loop will loop through until inventory is back to original inventory
        while snack_1[1] < 2 or snack_2[1] < 4 or snack_3[1] < 1:
            if snack_1[1] < 2:
                snack_1[1] += 1
                print("Adding Doritos")

            if snack_2[1] < 4:
                snack_2[1] += 1
                print("Adding Donuts")

            if snack_3[1] < 1: 
                snack_3[1] += 1 
                print("Adding Pretzels") 

        print("\n")  
        
    # state G will break out of the main while loop, thus shuting down the vending machine, (exiting out of the code)
    if state == 'G':
        print("\nVending machine turning off...\n")
        break