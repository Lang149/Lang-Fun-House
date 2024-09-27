print("Welcome to the Shipping Account Program!")
username = input("Hello! What is your username: ").title()
valid_usernames = ["Lang221", "Yamshippyhappyface",
                   "JamesIsTrueForYou", "Letsparty99", "Andy123"]
Shipping_Price = [5.10, 4.95, 4.60, 4.30]


def Shipping_Total(Amount): #Shipping total of all
    if 0 < Amount <= 100:
        Total = Shipping_Price[0] * Amount
    elif 100 < Amount <= 500:
        Total = Shipping_Price[1] * Amount
    elif 500 < Amount <= 1000:
        Total = Shipping_Price[2] * Amount
    elif Amount > 1000:
        Total = Shipping_Price[3] * Amount
    else:
        print(f"The value \"{Amount}\" is not a possible value.") #if amount is less than or equal to 0, give back this message
        Total = 0
    return Total #returns total value


def confirmation(confirm, cancel): #confirmation, confirms the order
    while True:
        print(f"Type {confirm} to confirm, type {cancel} to cancel.")
        confirmation_input = input("Input: ").upper()
        if confirmation_input == confirm:
            print(
                f"Your shipping order of {Shipping_Amount}, costing {Shipping_Total(Shipping_Amount)}$ has been sent, please check your email for the receipt.")
            break
        elif confirmation_input == cancel:
            print(
                f"Your shipping order of {Shipping_Amount}, costing {Shipping_Total(Shipping_Amount)}$ has been canceled.")
            break
        else:
            print("Your answer is not a vaild answer please try again.")


if username in valid_usernames: #actual function that gets printed
    capitalized_username = [username.capitalize() for username in username]
    print("Hello " + username + ". Welcome back to your account.")
    print("The current shipping prices are as follows:")
    print("Shipping orders 0 to 100: $5.10 each")
    print("Shipping orders 100 to 500: $5.00 each")
    print("Shipping orders 500 to 1000: $4.95 each")
    print("Shipping orders over 1000: $4.80 each")
    print("Hello!" + username +
          " How much shipping orders would you like to buy? ")
    Shipping_Amount = int(input("Shipping Order amount: "))
    print(f"Your shipping price is {Shipping_Total(Shipping_Amount)}$.")
    confirmation("Y", "N")
else:
    print("Sorry, you do not have an account with us. Goodbye.")
