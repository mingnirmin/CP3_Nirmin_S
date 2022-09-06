class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Jeon"
customer1.lastName = "Jungkook"
customer1.age = 25

customer2 = Customer()
customer2.name = "Lee"
customer2.lastName = "Jeno"
customer2.age = 22

customer3 = Customer()
customer3.name = "Lee"
customer3.lastName = "Dong-min"
customer3.age = 25

customer4 = Customer()
customer4.name = "Lee"
customer4.lastName = "Jong-suk"
customer4.age = 33

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()