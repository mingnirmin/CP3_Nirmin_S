menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        totalPrice += int(priceList[number])
    print("Total :", totalPrice, "THB")

while True:
    menuName = input("Please Enter Your Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()