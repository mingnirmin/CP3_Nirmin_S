print("Welcome to my shop, please enter your username and password")

usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "minnn" and passwordInput == "8899":
    print("**** Login successfully ****")
    print("**** You can choose the product ****")

    print(">>In-store items<<")
    print('''
    1. Chocolate flavored candy  5 THB
    2. Mint      flavored candy  5 THB
    3. Coke      flavored candy  5 THB
    4. Milk      flavored candy  5 THB
    ''')
    productSelected = int(input("Please select your product>> "))
    if productSelected == 1:
        productName = "Chocolate flavored candy"
        productPrice = 5
    elif productSelected == 2:
        productName = "Mint flavored candy"
        productPrice = 5
    elif productSelected == 3:
        productName = "Coke flavored candy"
        productPrice = 5
    elif productSelected == 4:
        productName = "MIlk flavored candy"
        productPrice = 5
    print("Product list of your choice: ", productName, ":", productPrice, "THB")
    amountOfCandy = int(input("please select QTY: "))
    print("Summary : ", productName, ":", amountOfCandy, "x", productPrice, "=", productPrice*amountOfCandy, "THB")
    print("**** Thank you for supporting our shop ****")
else:
    print("Your username or password is incorrect")