print("Welcome to the Shipping Account Program!")
username = input("Hello! What is your username: ")
valid_usernames = ["Lang221", "Yamshippyhappyface", "JamesIsTrueForYou", "Letsparty99", "Andy123"] #Chatgpt
if username in valid_usernames:
    capitalized_username =[username.capitalize() for username in username]
    print("Hello " + username + ". Welcome back to your account.")
    print("The current shipping prices are as follows:")
else:
    print("Sorry, you do not have an account with us. Goodbye.")
        if 0 < Shipping_Amount <= 200:
            Total = Shipping_Price[1] * Shipping_Amount
        elif 200 < Shipping_Amount <= 400:
            Total = Shipping_Price[2] * Shipping_Amount
        elif 400 < Shipping_Amount <= 800:
            Total = Shipping_Price[3] * Shipping_Amount
        else:
            Total = Shipping_Price[4] * Shipping_Amount
            
            
