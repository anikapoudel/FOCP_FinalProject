def pizza_price_calculator():
    print("BPP Pizza Price Calculator")
    print("==========================")

    while True:
        try:
            no_pizza = int(input("How many pizzas ordered?"))
            if no_pizza > 0:
                print(no_pizza)
                break
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")    
    
    while True:
        delivery = input("Is delivery required? (y/n) ").lower()
        if delivery == 'y' or delivery == 'n':
            print(delivery)
            break
        else:
            print('Please answer "Y" or "N".')
    
    while True:
        day = input("Is it Tuesday? (y/n) ").lower()
        if day == 'y' or day == 'n':
            print(day)
            break
        else:
            print('Please answer "Y" or "N".')

    while True:
        app = input("Did the customer use the app? (y/n) ").lower()
        if app == 'y' or app =='n':
            print(app)
            break
        else:
            print('Please answer "Y" or "N". ')


    # Calculate the total price based on the conditions
    pizza_cost = 12 # Base price for one pizza
    total_price = no_pizza * pizza_cost

    if delivery == 'y':
        total_price += 2.50  # Additional cost for delivery
    if delivery =='y' and no_pizza >= 5:
        total_price -=2.50

    if day == 'y':
        total_price *= 0.5  # 50% discount on Tuesdays

    if app == 'y':
        total_price *= 0.75  # 25% discount for app users

    # Display the total price
    print(f"\nTotal Price: £{total_price:.2f}")

# Call the function to run the program
pizza_price_calculator()
