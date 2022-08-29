def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "8888":
        return True
    else:
        return False
def showMenu():
    print("----ABC----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculator():
    vat = 7
    result = price + (price * 7 / 100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    price = price1 + price2
    print("Price + 7% vat =", price + (price * 7 / 100), "THB")

x = login()
if x == True:
    print(showMenu())
    y = menuSelect()
    if y == 1:
        price = int(input("Price (THB) : "))
        print("Price + 7% vat =", price + (price * 7 / 100), "THB")

    elif y == 2:
        priceCalculator()
    if True:
        print("DONE !!!")

else:
    print("Try again..")
    login()








