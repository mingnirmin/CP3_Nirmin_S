systemMenu = {"ข้าวผัดทะเล":50, "ข้าวผัดปู":60, "ก๋วยเตี๋ยว":45, "ราดหน้ากุ้ง":55}
menuList = []

def showBill():
    totalPrice = 0
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1],"THB")
        totalPrice += int(menuList[number][1])
    print("Total :", totalPrice, "THB")

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

print(menuList)
showBill()