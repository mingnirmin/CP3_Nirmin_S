userInput = "def"
passInput = "def"
usernameInput = "admin"
passwordInput = "8888"
while userInput != usernameInput or passInput != passwordInput:
    userInput = input("Username :")
    passInput = input("Password :")
    if userInput != usernameInput or passInput != passwordInput:
        print("Please try again")
print("Done !!!")


