print("Welcome to the Shipping Account Program!")
username = input("Hello! What is your username: ")
valid_usernames = ["Lang221", "Yamshippyhappyface", "JamesIsTrueForYou", "Letsparty99", "Andy123"] #Chatgpt
Shipping_Price = [5.10, 4.95, 4.60, 4.30]
if username in valid_usernames:
    capitalized_username =[username.capitalize() for username in username]
    print("Hello " + username + ". Welcome back to your account.")
    print("The current shipping prices are as follows:")
    Shipping_Amount = input(f"Hello! {username}, What amount of _ would you like to buy?")
    if 0 < Shipping_Amount <= 200:
        Total = Shipping_Price[1] * Shipping_Amount
        print(Total)
    elif 200 < Shipping_Amount <= 400:
        Total = Shipping_Price[2] * Shipping_Amount
        print(Total)
    elif 400 < Shipping_Amount <= 800:
        Total = Shipping_Price[3] * Shipping_Amount
        print(Total)
    else:
        Total = Shipping_Price[4] * Shipping_Amount
        print(Total)
else:
    print("Sorry, you do not have an account with us. Goodbye.")
            
