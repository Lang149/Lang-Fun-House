print("Welcome to the Shipping Account Program!")
username = input("Hello! What is your username: ")
valid_usernames = ["Lang221", "Yamshippyhappyface", "JamesIsTrueForYou", "Letsparty99", "Andy123"] #Chatgpt
Shipping_Price = [5.10, 4.95, 4.60, 4.30]
if username in valid_usernames:
    capitalized_username =[username.capitalize() for username in username]
    print("Hello " + username + ". Welcome back to your account.")
    print("The current shipping prices are as follows:")
    print("Shipping orders 0 to 100: $5.10 each")
    print("Shipping orders 100 to 500: $5.00 each")
    print("Shipping orders 500 to 1000: $4.95 each")
    print("Shipping orders over 1000: $4.80 each")
    Shipping_Amount = input("Hello!" + username + " How much shipping orders would you like to buy? ")
    if 0 < int(Shipping_Amount) <= 200:
        Total = Shipping_Price[1] * int(Shipping_Amount)
        print(Total)
    elif 200 < int(Shipping_Amount) <= 400:
        Total = Shipping_Price[2] * int(Shipping_Amount)
        print(Total)
    elif 400 < int(Shipping_Amount) <= 800:
        Total = Shipping_Price[3] * int(Shipping_Amount)
        print(Total)
    else:
        Total = Shipping_Price[4] * int(Shipping_Amount)
        print(Total)
else:
    print("Sorry, you do not have an account with us. Goodbye.")
